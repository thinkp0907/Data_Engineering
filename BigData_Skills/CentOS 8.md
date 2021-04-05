# CentOS 8

### CentOS 8 명령어

CentOS 8은 기존 CentOS 6 버전과는 조금의 변화가 있어보인다.

사용하는 명령어들이 많이 변화였으므로 약간에 편의성을 위해 미리 작성하겠다.

제일 중요하게 생각되는것은 대부분의 명령어들의 시작이 이제는 `systemctl` 을 붙여 된다는 것이다.

1. `systemctl get-default` : 현재 시스템에 디폴트 runlevel 확인

2. `systemctl set-default` <u>*TARGET.target*</u> : 현재 시스템에 디폴트 runlevel을 multi-user로 바꾸기
   ex) `systemctl set-default` <u>multi-user.target</u>

3. `systemctl restart NetworkManager.service`: 네트워크 서비스 재시작/ 

   >  기존 명령어 였던 `service network restart`를 대체 한 것 으로 생각됨

추가로 `chkconfig` 명령어와 `systemctl` 비교 표.

| service                        | systemctl                                                    | 설명                                        |
| ------------------------------ | ------------------------------------------------------------ | ------------------------------------------- |
| chkconfig <u>*name*</u> on     | systemctl enable *<u>name</u>*.service                       | 서비스 활성화 (부팅시 자동 구동)            |
| chkconfig *<u>name</u>* off    | systemctl disable *<u>name</u>*.service                      | 서비스 비활성화                             |
| chkconfig --list *<u>name</u>* | systemctl status *<u>name</u>*.service<br />systemctl is-enabled *<u>name</u>*.service | 서비스의 활성화 여부 표시                   |
| chkconfig --list               | systemctl list-unit-files --type service                     | 모든 서비스의 현재 활성화 여부 표시         |
| chkconfig --list               | systemctl list-dependencies --after                          | 지정한 target 이후에 시작하는 서비스를 표시 |
| chkconfig --list               | systemctl list-dependencies --before                         | 지정한  target 이전에 시작하는 서비스 표시  |

[출처:https://www.lesstif.com/system-admin/systemd-system-daemon-systemctl-24445064.html]

### vi 편집기 명령어



**[vi편집기 종료관련 명령어]**

| 명령어                                                       | vi 에디터에서 자주사용하는 종료관련 명령어                  |
| ------------------------------------------------------------ | ----------------------------------------------------------- |
| `:q`                                                         | vi에서 작업한것이 없을때 vi 종료                            |
| `:q!`                                                        | 작업한 내용을 저장하지 않고 종료                            |
| `:w[파일명]`<br />ex) :w /etc/sysconfig/network-scripts/ifcfg-eth0 | 작업한 내용을 저장만 한다. 파일명을 지정하면 새 파일로 저장 |
| `:wq`, `:wq!`                                                | 작업한 내용을 저장하고 vi를 종료                            |

**[vi편집기 삭제관련 명령어]**

| 명령어                     | vi에디터에서 자주사용하는 삭제관련 명령어                    |
| -------------------------- | ------------------------------------------------------------ |
| `x`, `[삭제할 글자 수]x`   | 커서가 위치한 글자를 삭제합니다.<br />x앞에 삭제할 글자수를 지정할수도 있습니다. |
| `dw`, `[삭제할 단어 수]dw` | 커서가 위치한 단어를 삭제합니다. <br />dw앞에 삭제할 단어수를 지정할수도 있습니다. |
| `dd`, `[삭제할 행 수]dd`   | 커서가 위치한 행을 삭제합니다. <br />dd앞에 삭제할 행의수를 지정할수도 있습니다. |
| `D`                        | 커서 위치로부터 행의 끝까지 삭제합니다.                      |
