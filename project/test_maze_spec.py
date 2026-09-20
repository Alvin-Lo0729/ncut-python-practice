"""
隨堂習題5 — 老鼠走迷宮：規格（測試先行，pytest 版）

執行方式（在專案根目錄）：
    pytest project/test_maze_spec.py            # 跑全部
    pytest project/test_maze_spec.py -v         # 一個一個列出來
    pytest project/test_maze_spec.py -x         # 第一個失敗就停（推薦！）
    pytest project/test_maze_spec.py -k is_goal # 只跑名字含 is_goal 的

怎麼用：
  1. 現在只有 Step 1 的測試是開著的，其他都被 @pytest.mark.skip 關起來。
  2. 跑測試 -> 看它紅 -> 打開 test5_Mouse_9B417004.py 實作 -> 再跑 -> 變綠。
  3. 綠了之後，把下一個 Step 的 @pytest.mark.skip 那行刪掉，繼續。
  4. 一次只解一個測試。不要偷跑。
"""
import pytest

from test5_Mouse_9B417004 import (
  MAZE, is_goal, next_steps, find_all_paths, bfs_shortest_path, format_path,
)

# --- 測試用的小迷宮（小到可以用眼睛驗證答案）-----------------------------

OPEN_2X2 = [[0, 0],
            [0, 0]]

CORRIDOR = [[0, 1, 1],          # 只有一條路：往下走到底，再往右走到底
            [0, 1, 1],
            [0, 0, 0]]

BLOCKED = [[0, 1],              # 對角線被切斷，走不到終點
           [1, 0]]

WIDE_3X5 = [[0, 0, 0, 0, 0],    # 故意做成「非正方形」，抓死板的 len(maze) 寫法
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]]

THETA = [[0, 0, 0, 0, 0],       # 中間多一條通道 -> 有捷徑也有繞遠路
         [0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0]]


# ================================================================ Step 1
class TestIsGoal:
  """要有方法確認『是否到終點了』。"""

  def test_bottom_right_corner_is_the_goal(self):
    assert is_goal(OPEN_2X2, (1, 1)) is True

  def test_start_is_not_the_goal(self):
    assert is_goal(OPEN_2X2, (0, 0)) is False

  def test_one_cell_maze_start_is_already_the_goal(self):
    assert is_goal([[0]], (0, 0)) is True

  def test_goal_of_a_non_square_maze(self):
    # 3 列 5 行 -> 終點是 (2, 4)，不是 (2, 2)
    assert is_goal(WIDE_3X5, (2, 4)) is True
    assert is_goal(WIDE_3X5, (2, 2)) is False


# ================================================================ Step 2
class TestNextSteps:
  """要有方法確認『還有沒有其他路可以走』。DFS 和 BFS 共用這個零件。"""

  def test_does_not_fall_off_the_top_or_left_edge(self):
    # 在 (0,0)，上面和左邊都是外面 -> 只剩右邊和下面
    # 小心：Python 的 maze[-1] 不會出錯，它會繞到最後一列！
    assert sorted(next_steps(OPEN_2X2, (0, 0), {(0, 0)})) == [(0, 1), (1, 0)]

  def test_does_not_fall_off_the_bottom_or_right_edge(self):
    assert sorted(next_steps(OPEN_2X2, (1, 1), {(1, 1)})) == [(0, 1), (1, 0)]

  def test_walls_are_not_walkable(self):
    # CORRIDOR 的 (0,0)：右邊 (0,1) 是牆 -> 只能往下
    assert sorted(next_steps(CORRIDOR, (0, 0), {(0, 0)})) == [(1, 0)]

  def test_already_visited_cells_are_not_returned(self):
    # (0,1) 已經走過了 -> 不能再回頭
    assert sorted(next_steps(OPEN_2X2, (0, 0), {(0, 0), (0, 1)})) == [(1, 0)]

  def test_dead_end_returns_empty_list(self):
    assert next_steps(BLOCKED, (0, 0), {(0, 0)}) == []


# ================================================================ Step 3
@pytest.mark.skip(reason="Step 3：Step 2 全綠之後，把這一行刪掉")
class TestFindAllPaths:
  """【DFS + 回溯】要收集『每一條』路徑的完整內容。"""

  def test_one_cell_maze_has_a_single_trivial_path(self):
    assert find_all_paths([[0]]) == [[(0, 0)]]

  def test_corridor_has_exactly_one_path(self):
    assert find_all_paths(CORRIDOR) == [
      [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    ]

  def test_open_2x2_has_exactly_two_paths(self):
    # 走右再走下，或走下再走右。順序不重要，內容要對。
    assert sorted(find_all_paths(OPEN_2X2)) == sorted([
      [(0, 0), (0, 1), (1, 1)],
      [(0, 0), (1, 0), (1, 1)],
    ])

  def test_unreachable_goal_gives_no_paths(self):
    assert find_all_paths(BLOCKED) == []

  def test_finds_the_long_detour_too_not_just_the_short_ones(self):
    # THETA 有 4 條路：3 條長度 7 的捷徑，外加 1 條長度 11 的繞遠路。
    # 如果你的 visited 沒有「回溯」，就會少找到路徑。
    paths = find_all_paths(THETA)
    assert len(paths) == 4
    assert sorted(len(p) for p in paths) == [7, 7, 7, 11]


# ================================================================ Step 4
@pytest.mark.skip(reason="Step 4：Step 3 全綠之後，把這一行刪掉")
class TestBfsShortestPath:
  """【BFS + 佇列】一層一層擴散，第一個碰到終點的就是最短。"""

  def test_one_cell_maze(self):
    assert bfs_shortest_path([[0]]) == [(0, 0)]

  def test_corridor_returns_the_only_path(self):
    assert bfs_shortest_path(CORRIDOR) == [
      (0, 0), (1, 0), (2, 0), (2, 1), (2, 2)
    ]

  def test_unreachable_goal_returns_none(self):
    assert bfs_shortest_path(BLOCKED) is None

  def test_returns_an_actual_path_not_just_a_number(self):
    path = bfs_shortest_path(OPEN_2X2)
    assert path[0] == (0, 0)
    assert path[-1] == (1, 1)
    assert len(path) == 3

  def test_picks_the_shortcut_and_ignores_the_detour(self):
    # THETA 最短是 7（有 3 條並列）。BFS 絕不該回傳那條長度 11 的。
    assert len(bfs_shortest_path(THETA)) == 7


# ================================================================ Step 5
@pytest.mark.skip(reason="Step 5：Step 4 全綠之後，把這一行刪掉")
class TestFormatPath:
  """輸出格式：R1 (31)=> [0,0],[0,1],[0,2]..."""

  def test_formats_name_step_count_and_cells(self):
    assert format_path("R1", [(0, 0), (0, 1), (1, 1)]) == \
           "R1 (3)=> [0,0],[0,1],[1,1]"

  def test_formats_a_single_cell_path(self):
    assert format_path("Best", [(0, 0)]) == "Best (1)=> [0,0]"


# ================================================================ Step 6
@pytest.mark.skip(reason="Step 6：Step 5 全綠之後，把這一行刪掉")
class TestRealMaze:
  """跑真正的 16x16 迷宮。

  這裡不寫死答案（寫死就等於把答案給你了），改成檢查「一條合法路徑該有的性質」，
  以及「兩套演算法的答案要互相對得起來」。你的程式只要對，就會全綠。
  """

  @pytest.fixture(scope="class")
  def paths(self):
    return find_all_paths(MAZE)

  def test_dfs_finds_at_least_one_path(self, paths):
    assert len(paths) > 0

  def test_every_path_starts_at_top_left_and_ends_at_bottom_right(self, paths):
    for path in paths:
      assert path[0] == (0, 0)
      assert path[-1] == (15, 15)

  def test_no_path_ever_walks_through_a_wall(self, paths):
    for path in paths:
      for (r, c) in path:
        assert MAZE[r][c] == 0, f"{(r, c)} 是牆壁"

  def test_every_move_is_one_step_up_down_left_or_right(self, paths):
    for path in paths:
      for (r1, c1), (r2, c2) in zip(path, path[1:]):
        assert abs(r1 - r2) + abs(c1 - c2) == 1, \
          f"{(r1, c1)} 跳到 {(r2, c2)} 不是合法的一步"

  def test_a_path_never_steps_on_the_same_cell_twice(self, paths):
    for path in paths:
      assert len(path) == len(set(path)), "路徑裡有重複的格子"

  def test_bfs_result_is_also_a_legal_path(self):
    best = bfs_shortest_path(MAZE)
    assert best[0] == (0, 0)
    assert best[-1] == (15, 15)
    for (r1, c1), (r2, c2) in zip(best, best[1:]):
      assert MAZE[r2][c2] == 0
      assert abs(r1 - r2) + abs(c1 - c2) == 1

  def test_bfs_and_dfs_agree_on_the_shortest_length(self, paths):
    # 兩套演算法互相驗證：BFS 找到的長度，應該等於 DFS 所有路徑裡最短的那個。
    # 這一條如果紅了，代表其中一邊寫錯了。
    assert len(bfs_shortest_path(MAZE)) == min(len(p) for p in paths)
