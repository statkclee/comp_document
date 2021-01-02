---
layout: page
title: Computational Documents
subtitle: 데이터 과학 문서
---

> ### AI is a Superpower {.callout}
>
> "AI is a superpower!!!", 인공지능을 체득하면 슈퍼파워를 손에 쥘 것이다. [Andrew Ng](https://twitter.com/andrewyng/status/728986380638916609)
>
> 금수저, 은수저 슈퍼파워를 받은 사람과 기계학습을 통달한 흑수저들간의 무한경쟁이 드뎌 시작되었다. 물론, 
> 금수저를 입에 물고 기계학습을 통달한 사람이 가장 유리한 출발을 시작한 것도 사실이다.

<img src="fig/comp-documents-overview.png" alt="computational documents" width="100%" />

## 학습목차 

1. **인코딩, 글꼴**
    * [R 유니코드, 인코딩](regex-encoding.html)
    * [R 정규표현식](regex-r.html)
    * [정규표현식과 문자데이터 - `regexplain`](regex-r-char.html)
    * [자연어처리(NLP) - 정규표현식](http://statkclee.github.io/nlp)
    * [R마크다운 글꼴(font)](cd-fonts.html)
1. [현대적인 과학논문 저작](http://statkclee.github.io/modern-scientific-authoring/index-kr.html)
    * [심각한 현재 상황](http://statkclee.github.io/modern-scientific-authoring/01-mess-kr.html)
    * [마크다운 기초](http://statkclee.github.io/modern-scientific-authoring/02-markdown-kr.html)
    * [고급 마크다운](http://statkclee.github.io/modern-scientific-authoring/03-advanced-kr.html)
    * [R 마크다운 실무](rmarkdown-in-production.html)
    * [자주 사용되는 $\LaTeX$ 수식](cd-latex.html)
    * [이광춘, 주용우 (2020), "사람과 기계의 일자리 경쟁 요인과 협업 방안", 한국디지털경영학회](automation-kasdba.html)
1. [`RStudio` 워드 프로세서: `hunspell`](cd-rstudio-wp.html)
    * [GIF 동영상 제작 - 맥OS](cd-gif.html)
1. **[R 콘텐츠: 블로그, 이력서 등](cd-netlify.html)**
    * [정적 웹서비스 개발 툴체인](devops-dev-vm.html) 
        * [윈도우 정적 웹서비스 개발 툴체인](devops-dev-vm-windows.html) 
    * [Github - 블로그](ds-github-blog.html)
    * [GITHUB `readme.md`](ds-github-readme.html)
    * [블로그 - blogdown](ds-blogdown.html)
        * [R마크다운 보고서 패스워드 보안](ds-netlify-protection.html)
    * [이력서(Resume)](ds-resume.html)
    * [북다운(bookdown)](bookdown-intro.html)
        * [출판 자동화(DevOps)](bookdown-github-travis.html)
    * [R 노트북(Notebook)](ds-notebook.html)
    * [R 발표자료(Slideshows) - `xaringan`](ds-presn.html)
        * [`xaringan` 기본기능](cd-xaringan-basics.html)
        * [파워포인트 `pptx` 발표자료](ds-pptx-rmarkdown.html)
    * [보고서 자동화](ds-report-automation.html)
1. [대쉬보드(Dashboard)](cd-dashboard.html)
    - [코로나19](cd-corona.html)
    - [`GitHub` 호스팅](cd-github-hosting.html)
    - [약국 마스크 실시간 대쉬보드](cd-realtime-mask.html)
1. Computational Documents Tutorial
    - [R 마크다운](tutorial/01_rmarkdown/bmi.html)
    - **Parameterized Documents**
        - [기본 문서](tutorial/02_parameterized_rmd/election.html)
        - [매개변수 적용된 문서](tutorial/02_parameterized_rmd/election-province.html)
        - [자동 문서 생성 스크립트](tutorial/02_parameterized_rmd/automate-province-report.R)
    - [인터랙티브 문서](tutorial/03_interactive_rmd/election-interactive.html)
    - [$\LaTeX$ `PDF` 문서](comp_doc_pdf.html)
    - [R마크다운 코드 덩어리(Code Chunk)](cd-code-chunk.html)    
1. Compendium ... R 프로젝트: (특정 주제에 대한) 개요서
    - [개요서(Compendium) 시작하며](cd_compendium.html)
    - [시작이 반이다 - `start small`](cd-start-small.html)
    - [팩키지 개발](cd-pkg-development.html)
    - [윈도우즈 stat545 - `Makefile`](automation-makefile.html)
    - **트위터 보고서**
        - R 마크다운 보고서: [다양한 데이터 가져오기 - "트위터 데이터 과학"](https://statkclee.github.io/ingest-data/ingest-twitter-data-science.html)
        - `Makefile` 자동화 보고서: [Computational Documents - "Makefile - PDF, HTML, DOCX"](compendium.html)
            - [GitHub: Compendium 301](https://github.com/statkclee/compendium_301)
    - [`rocker` 도커 컨테이너](cd-docker-rstudio.html)
    - [`rocker` 도커 컨테이너 - `Dockerfile` & `Docker Hub`](cd-docker-rstudio-dockerfile.html)
1.  [데이터 과학 개발운영 아키텍처](devops-dev-vm-arch.html)
    * [객체 저장소 FTP 배포(Deployment)](devops-ftp-object-storage.html)
    * [개발운영(DevOps) 실습예제 - 컴퓨터 과학 언플러그드](devops-pracitce.html)
1. [문서 프로그래밍 - 한글 $LaTeX$ 사전준비](latex.html)
    * [한글 LaTeX 소개](latex-intro.html)
    * [한글 LaTeX 윈도우 설치](latex-install-windows.html)
    * [한글 LaTeX 설치환경 가상화](latex-virtual.html)
    * [한글 LaTeX 편집기](latex-utils.html)
    * [파이썬 스핑크스](latex-sphinx.html)
1. [파이썬 빌드 doit](doit-index.html)
    * [doit 설치하기](doit-install.html)
    * [doit 시작하기](doit-basics.html)
    * [부작업(Sub-tasks)](doit-sub_tasks.html)
    * [분석결과가 최신상태인지 점검하기](doit-uptodate.html)
1. [출판사, 저널, 논문 API](publisher-journal-api.html)
    * [논문 저자: `rorcid`](author-orcid.html)
    * [상호참조: `crossref`](paper-crossref.html)

> ### 원문 출처 및 저작 라이선스 {.getready}
>
> 이 번역의 원작 "[Modern Scientific Authoring](http://swcarpentry.github.io/modern-scientific-authoring/)"은 과학 컴퓨팅을 위한 소프트웨어 교육을 추진하는 
> [소프트웨어 카펜트리](http://software-carpentry.org/) 재단에서 개발하여 공개한 교재에 영감을 받아 준비 되었다.
> 이 교재는 크리에이티브 커먼스(Creative Commons)의 저작자표시(BY, Attribution), 동일조건변경허락(SA, Share-Alike) 라이선스[https://creativecommons.org/licenses/by-sa/2.0/kr/](https://creativecommons.org/licenses/by-sa/2.0/kr/)를 준용합니다.



### [xwMOOC 오픈 교재](https://statkclee.github.io/xwMOOC/)

- **컴퓨팅 사고력(Computational Thinking)**
    - [컴퓨터 과학 언플러그드](http://statkclee.github.io/unplugged)  
    - [리보그 - 프로그래밍과 문제해결](https://statkclee.github.io/code-perspectives/)  
         - [러플](http://statkclee.github.io/rur-ple/)  
    - [파이썬 거북이](http://swcarpentry.github.io/python-novice-turtles/index-kr.html)  
    - [정보과학을 위한 파이썬](https://statkclee.github.io/pythonlearn-kr/)  
        + [정보 과학을 위한 R - R for Informatics](https://statkclee.github.io/r4inf/)
    - [소프트웨어 카펜트리 5.3](http://statkclee.github.io/swcarpentry-version-5-3-new/)
    - [기호 수학(Symbolic Math)](https://statkclee.github.io/symbolic-math/)
    - [데이터 과학을 위한 R 알고리즘](https://statkclee.github.io/r-algorithm/)
    - [데이터 과학을 위한 저작도구](https://statkclee.github.io/ds-authoring/)
        - [The Official xwMOOC Blog](https://xwmooc.netlify.com/)
    - [비즈니스를 위한 오픈 소스 소프트웨어](http://statkclee.github.io/open-source-for-business/)    
- **데이터 과학**
    - [R 데이터과학](https://statkclee.github.io/data-science/)
    - [시각화](https://statkclee.github.io/viz/)
    - [Computational Document](https://statkclee.github.io/comp_document/)
    - [데이터 과학– 기초 통계](https://statkclee.github.io/statistics/)    
        - [공개 기초 통계학 - OpenIntro Statistics](https://statkclee.github.io/openIntro-statistics-bookdown/)
    - [보안 R](https://statkclee.github.io/security/) - TBA
    - **다양한 데이터**
        + [텍스트 - 자연어처리(NLP)](https://statkclee.github.io/text/)
        + [네트워크(network)](https://statkclee.github.io/network)
        + [공간통계를 위한 데이터 과학](https://statkclee.github.io/spatial/)        
        + [고생대 프로젝트](http://statkclee.github.io/trilobite)
        + [금융(finance)](https://statkclee.github.io/finance/)
        + [자동차 데이터 분석](https://statkclee.github.io/automotive/)
        + 비즈니스 프로세스(Business Process) - bupar
    - **모형**
        + [데이터 과학 - 모형](https://statkclee.github.io/model/)
    - [~~R 팩키지~~](http://r-pkgs.xwmooc.org/)
    - [~~통계적 사고~~](http://think-stat.xwmooc.org/)
- **빅데이터**
    - [빅데이터(Big Data)](http://statkclee.github.io/bigdata)
    - [데이터 제품](https://statkclee.github.io/data-product/)
    - [R 도커](http://statkclee.github.io/r-docker/)
- **기계학습, 딥러닝, 인공지능**
    - [고성능 컴퓨팅(HPC)](http://statkclee.github.io/hpc)
    - [기계학습](http://statkclee.github.io/ml)
    - [딥러닝](http://statkclee.github.io/deep-learning)
    - [R 병렬 프로그래밍](http://statkclee.github.io/parallel-r/)
    - [인공지능 연구회](https://statkclee.github.io/ai-lab/)
- [IoT 오픈 하드웨어(라즈베리 파이)](http://statkclee.github.io/raspberry-pi)
    - [$100 오픈 컴퓨터](https://statkclee.github.io/one-page/)   
    - [$100 오픈 슈퍼컴퓨터](https://statkclee.github.io/hpc/)
- [선거와 투표](http://statkclee.github.io/politics)
    - [저녁이 있는 삶과 새판짜기 - 제7공화국](https://statkclee.github.io/hq/)
    - [대한민국 제21대 국회의원 선거](https://statkclee.github.io/election/)


