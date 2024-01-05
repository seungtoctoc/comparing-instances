<h4>인스턴스 유형에 따른 성능 측정 결과 (시간 빠른 순)</h4>
  🌑 크롤링 전 시간과 크롤링 후 시간의 차이를 계산<br>
  🌑 t, m, c, r 인스턴스의 가장 최근 세대에서 large<br>
  🌑 소수점 9번째 자리에서 반올림<br><br>

  <b>r6id.large</b>, x86_64 : 7.87345433<br>
  <b>c6in.large</b>, x86_64 : 8.51436973<br>
  <b>m4.large</b>, x86_64 : 9.42785406<br>
  <b>t3a.large</b>, x86_64 : 9.80416965<br><br>

  ⭐️<br>
  R : 메모리<br>
  “<b>R6id</b> 인스턴스는 <b>메모리 사용이 많은</b> 워크로드, 분산 웹 규모 인 메모리 캐시, 인 메모리 데이터베이스 및 실시간 빅 데이터 분석에 매우 적합합니다.”<br>

  🌑 워크로드 : 작업에 소요되는 리소스, 시간<br>
  🌑 인 메모리 캐시 : 메모리(RAM)에 보관하는 캐시<br>
  🌑 인 메모리 데이터베이스 : 메모리에 보관하는 데이터베이스<br><br>

  ⭐️<br>
  C : 컴퓨팅. 최고 성능 프로세서<br>
  “<b>C6in</b> 인스턴스는 EC2 인스턴스 전체에서 <b>최고 수준</b>의 Amazon EBS 성능이 제공됩니다.”<br>
  🌑 EBS : Elastic Block Store.<br><br>

  ⭐️<br>
  M : 리소스 균형적 사용<br>
  ”<b>M4</b> 인스턴스는 웹 서버, 데이터베이스, caching fleets 및 엔터프라이즈 애플리케이션과 같은 <b>다양한 워크로드</b>에 적합합니다.”<br>
  🌑 fleet
  <img width="670" alt="스크린샷 2024-01-05 오전 8 25 34" src="https://github.com/seungtoctoc/seungtoctoc/assets/102455571/f8d4b4aa-e82c-499c-b8e5-ae50caa65dcb"><br>
  🌑 엔터프라이즈 애플리케이션 : 조직에서 사용하는 컴퓨터 소프트웨어<br><br>

  ⭐️<br>
  T : 성능 순간 확장<br>
  “<b>T3A</b> 인스턴스는 높은 컴퓨팅 성능을 지속할 필요는 없지만, 사용량에서 일시적으로 <b>스파이크</b>가 발생하는 워크로드에 매우 적합합니다.”<br><br>


  ------
  <h4>인스턴스 크기 별 비교</h4>


  * Tg4 인스턴스 <br><br>
이러한 인스턴스는 기본 수준의 CPU 성능 외에 버스트 기능이 있어 워크로드에 필요한 만큼 성능을 높일 수 있습니다. 무제한 인스턴스는 필요할 때마다 원하는 기간 동안 높은 CPU 성능을 유지할 수 있습니다. 자세한 내용은 성능 순간 확장 가능 인스턴스 섹션을 참조하세요. 이러한 인스턴스는 다음의 경우에 적합합니다.<br><br>

    웹 사이트 및 웹 애플리케이션: <br>
    코드 리포지토리 <br>
    개발, 빌드, 테스트 및 스테이징 환경<br>
    마이크로서비스 <br><br>
    

* 인스턴스 별 성능 결과 <br><br>
<img width="444" alt="스크린샷 2024-01-04 오후 4 43 00" src="https://github.com/godltjsdud/godltjsdud/assets/71091090/a608481d-b5b9-45b2-be9c-61ce13ebd703"><br>
<img width="442" alt="스크린샷 2024-01-04 오후 4 35 46" src="https://github.com/godltjsdud/godltjsdud/assets/71091090/0875c67a-95e9-406a-99f3-ee7447939c8c"><br>
<img width="448" alt="스크린샷 2024-01-04 오후 4 29 42" src="https://github.com/godltjsdud/godltjsdud/assets/71091090/622e8732-2791-4a40-81ee-ba37289ec929"><br>
<img width="441" alt="스크린샷 2024-01-04 오후 4 51 42" src="https://github.com/godltjsdud/godltjsdud/assets/71091090/3a43c96a-01a1-4688-a4f9-13f45a2422b6"><br>
```
  t4g.micro : 5789ms 
  t4g.nano : 5989ms 
  t4g.small : 5810ms 
  t4g.medium :  6149ms

  micro < small < nano < medium
```
<br>

* 하드웨어 사양<br>
    | 인스턴스 유형 | 기본 vCPU | 메모리(GIB) |
    | ------- | ------- | ------- |
    | t4g.nano | 2 | 0.50 |
    | t4g.micro | 2 | 1.00 |
    | t4g.small | 2 | 2.00 |
    | t4g.medium | 2 | 4.00 |
<br><br>
<br>