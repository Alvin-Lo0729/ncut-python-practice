"""pytest 設定檔。

這個檔案本身是空的，但「它存在於專案根目錄」這件事就有作用：
pytest 看到根目錄有 conftest.py，就會把專案根目錄加進 sys.path，
測試檔裡的 `from subject.W3HW import ...` 才找得到 subject 這個資料夾。

沒有它的話，只有 `python -m pytest` 能跑（因為 -m 會自動把目前目錄加進
sys.path），直接打 `pytest` 會噴 ModuleNotFoundError: No module named 'subject'。
"""
