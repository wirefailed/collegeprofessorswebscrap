# collegeprofessorswebscrap

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Web Scrapper for College Professor's educational background utilizing Python and Beautiful Soup 4. The project grabs data from a set URL - in this case the USC Viterbi faculty page. From the faculty page, the webscraper finds all the professor's individual pages. Afterwards, the webscraper then scrapes each professor's individual page to college information such as name, occupation, and degrees from the individual professor. We have accounted for possible internet errors through keeping track of the URLs of professors the first run did not receive information for. The data is then stored in a local database by last name order.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Python,
Beautiful Soup 4,
PostgresSQL

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Install postgresSQL 
Inside postgresSQL, create database called 'collegeprofessorinfos'

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```zsh
   git clone https://github.com/wirefailed/collegeprofessorswebscrap.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Run main.py and answer all the questions
   ```zsh
   python main.py
   ```
  
   <img width="500" alt="Screenshot_2024-06-24_at_9 54 14_AM" src="https://github.com/wirefailed/collegeprofessorswebscrap/assets/131930750/439f9fa3-8649-4790-94ab-72654d12b885">
   <img width="500" alt="Screenshot_2024-06-24_at_9 54 45_AM" src="https://github.com/wirefailed/collegeprofessorswebscrap/assets/131930750/ab086c91-ae43-4fa2-b64f-ae57312699e8">

   As shown on the image, it will store it like this on PostgresSql

2. Search professors' backgrounds by running `searchingalgorithm.py`
   ```zsh
   python searchingalgorithm.py
   ```

   For example, the result will come out like this:
<img width="500" alt="Screenshot 2024-06-29 at 9 47 06 PM" src="https://github.com/wirefailed/collegeprofessorswebscrap/assets/131930750/b8b5366d-f846-4ec0-b88e-4308c2e2661d">


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Install BeautifulSoup4 and psycopg2
- [x] Go to https://viterbi.usc.edu/directory/faculty and understand its properties in HTML
- [x] Use BeautifulSoup4 to get a list of all professors with link that accesses to their personal website
- [x] Once again, understand how each website contains data and use BeautifulSoup4 to store in multi dimensional array
- [x] Use psycopg2 to store the list of professors and their occupations inside one table
- [x] Create another table that stores their degrees with foreign key that connects both tables
- [x] Create another file that help searches professors' degrees using PostgresSQL using Join, LIKE, and etc...

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Junsoo Kim, Phong Nguyen

Project Link: [https://github.com/wirefailed/collegeprofessorswebscrap.git](https://github.com/wirefailed/collegeprofessorswebscrap.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [GitHub Pages](https://pages.github.com)
* [beautifulsoup4 Page](https://pypi.org/project/beautifulsoup4/)
* [psycopg Page](https://www.psycopg.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



