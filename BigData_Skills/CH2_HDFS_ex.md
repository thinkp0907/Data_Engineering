## Chapter 02 빅데이터 파일럿 프로젝트

### Sample.txt 업로드 예제

- Sample.txt 파일 업로드

  - 파일질라 FTP 클라이언트 실행

  - Server02에 SFTP 접속

    호스트: server02.hadoop.com

    사용자명: bigdata

    비밀번호: bigdata

    포트: 22

    연결후 Sample.txt 파일을 Server02의 /home/bigdata/ 경로에 업로드





### HDFS에 파일 저장

먼저 Server02에 SSH 접속을 하고 업로드한 샘플 파일이 있는 위치로 이동해서 HDFS의 put 명령 실행

`$ cd /home/bigdata/`

`$ hdfs dfs -put Sample.txt /tmp` 

Sample.txt 파일을 HDFS의 /tmp 디렉터리로 저장



### HDFS에 저장한 파일 확인

`$ hdfs dfs -ls /tmp`

앞서 /tmp 디렉터리에 저장한 `Sample.txt` 파일의 목록 조회



### HDFS에 저장한 파일 내용보기

`$hdfs dfs -cat /tmp/Sample.txt`

"Sample.txt" 파일의 내용을 보여준다.



### HDFS에 저장한 파일 상태 확인

`$ hdfs dfs -stat '%b %o %r %u %n' /tmp/Sample.txt`

파일크기(%b), 파일 블록 크기(%o), 복제 수(%r), 소유자명(%u), 파일명(%n) 정보를 보여준다.



### HDFS에 저장한 파일의 이름 바꾸기

`$ hdfs dfs -mv /tmp/Sample.txt /tmp/Sample2.txt`

기존 파일명인 "Sample.txt"를 "Sample2.txt"로 변경한다.

​	

### HDFS의 파일 시스템 상태 검사

`$ hdfs fsck /`

전체 크기, 디렉터리 수, 파일 수, 노드 수 등 파일 시스템의 전체 상태를 보여준다.

`$ hdfs dfsadmin -report`

하둡 파일시스템의 기본 정보 및 통계를 보여준다.



### HDFS에 저장된 파일을 로컬 파일시스템으로 가져오기

`$ hdfs dfs -get /tmp/Sample2.txt`

로컬의 /home/bigdata 디렉터리에 Sample2.txt 파일이 생성된다.



### HDFS의 저장한 파일 삭제(휴지통)

`$ hdfs dfs -rm /tmp/Sample2.txt`

삭제 명령을 실행하면 우선 휴지통에 임시 삭제되며, 복구가 가능하다. 휴지통으로 임시 삭제된 파일은 특정 시간이 지나면 자동으로 완전 삭제된다.

휴지통에 임시 삭제가 필요 없을 때는 -skipTrash 옵션을 이용한다.



