<img alt="localhost_8000_ (3)" src="https://github.com/user-attachments/assets/ef5b229d-ba1b-40f6-884c-f11e18e21292" />

<!-- <img width="2184" height="1396" alt="localhost_8000_ (2)" src="https://github.com/user-attachments/assets/5c2a5d87-b9a2-4a27-a33d-318433ad31b7" /> -->


# MCK Schedule
MCK Schedule is a web app for convenient browsing of univercity lecture schedule.

Built as a server-side rendering web app with Python, FastAPI, MySQL, Jinja2 (template engine), HTML, CSS, JavaScript

## Idea
I've joined a sertain univercity department (which abbreviation is MCK). I was looking for ideas for a pet project when I saw our schedule. It was awful and extremely inconvenient, so I spent a few weekends and created this website.

The department had about 10 groups, each having several subgroups, each having slightly different lecture schedule. The original printed timetable looked like a grid with classes as it's cells. The issue - it was sorted not for each group, but for classrooms. So to figure out whether you have a class now or not, you'd had to check the entire row.

## Features
- <details> 
    <summary>Cool randomly generated home page</summary> 
    
    <img  alt="home-page-random" src="https://github.com/user-attachments/assets/b204b5d2-7d01-431f-872f-e72e925b86fe" />
    
      Each time chooses some random real lectures for the scattered and the ordered layouts, as well as groups and subgroups for the suggestsions
   </details>
- <details> 
    <summary>Language selection: supports english, russian, polish and ukranian</summary> 
    
    <img width="800" height="546" alt="home-page-languages" src="https://github.com/user-attachments/assets/b98a3d17-9493-4e8b-a13d-38a065af2932" />

  Stores selected language in a cookie or if absent uses `Accept-Language` header; stores translation strings in json files and shows corresponding ones
   </details>
- Search bar with typehints, allowing to find any group / subgroup / teacher / classroom. If the search query matches some entry, redirects user to the entry's page, otherwise to search results page
- Multiple semesters support
- Page-specific notifications
- Favourite schedules (saved to cookies)
- Statistics page, counting times anyone entered specific schedule page

## Database structure
<img width="800" alt="Diagram - local 4" src="https://github.com/user-attachments/assets/3f39db62-0055-4262-9be2-6e8669b0ce88" />
<!-- width="1234" height="837" -->
<!-- <img width="1248" height="854" alt="Diagram - local 3" src="https://github.com/user-attachments/assets/89678e24-12c8-4d6d-8a40-ea554262cb19" /> -->

<!-- <img width="625" height="435" alt="Diagram - local-2" src="https://github.com/user-attachments/assets/b2667af2-32d6-486b-9b62-35cfaf390cab" /> -->

The app uses MySQL to store all the data. It has 11 tables. It has semesters, subjects, teachers and classrooms as separate tables and a lessons table related to all of them. This approach allows type-hint options when creating a new lecture, keep all data consistent and simultaneously change classroom's name, teacher's initials, etc. Furthermore, there is a table for groups and one for their subgroups, and two junction tables relating groups-lessons and subgroups-lessons. There are also two standalone tables, statistics and user accounts



## Pages

- <details> 
  <summary>Home page</summary> <img width="2160" height="3267" alt="localhost_8000_" src="https://github.com/user-attachments/assets/89b2234f-80fc-47ee-8a91-c5c7c809367f" /></details>
- Schedule pages
  - Group schedule
  - <details> 
    <summary>Subgroup schedule</summary> <img width="2160" height="3140" alt="localhost_8000_group_4S_art" src="https://github.com/user-attachments/assets/b0438225-2259-4d80-bde2-24424ad043ec" /></details>
  - Teacher schedule
  - Classroom schedule
- Search results 
- About
- Changelog
- <details> 
  <summary>Statistics</summary> <img width="2184" height="1396" alt="localhost_8000_statistics" src="https://github.com/user-attachments/assets/6b6bb07f-1970-4d43-b757-9b130f58c6cc" />></details>
- Error page

## Availabilty 

Used to be available at https://mck.chel0.dev until May 2026, when the lectures ended. Was hosted on Zaebur free tier, which is unfortunately no longer provided. 

## Contributors

Many thanks to:
- [Ihor Lysiuk](https://github.com/igorlysiuk043-cyber) for the ukranian translation

<!-- <details> <summary>123</summary>
<img width="2160" height="3267" alt="localhost_8000_" src="https://github.com/user-attachments/assets/89b2234f-80fc-47ee-8a91-c5c7c809367f" /></details> -->
