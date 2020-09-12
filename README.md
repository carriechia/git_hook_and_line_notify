當專案沒有放在任何的lab上（gitlab github ...etc），只有使用檔案更新，可以利用git hook 來發送 commit 通知。


### 使用 git hook 執行 python 並發送 Line 群組通知
git hook 是 Git 提供的事件觸發 script 腳本，sample 檔都會放在 Repository `.git/hooks` 內，此專案選用 Server-side hooks 的 post-receive （在整個過程執行完後執行，可以用來更新其他系統或通知）

### 直接把三個檔案複製到.git/hooks內 (注意！ hooks 必須是放在 server 內的 git repository)
`cp -r post-receive repository_name/.git/hooks`
`cp -r post-receive.py repository_name/.git/hooks`
`cp -r config.ini repository_name/.git/hooks`

#### config.ini 內加入line notify 申請對應的聊天室權杖
`channel_access_token` = "token"

#### project name 是自定義的（更新專案使用的名稱）
`project_name` = "專案名稱"

#### post-receive.py 是通知 line notify 的執行檔案 config.ini 要和此檔放在同一層，如果要直接執行發送，也可執行以下指令
`python3 post-receive.py`