# Introduction
When shopping for a new car, one of the most important factors is the vehicle's efficiency. Most modern vehicles are far more efficient than cars in years past, but some models outperform others.

This project contains the fuel economy trend data from Car and Driver Magazine, an American automotive enthusiast magazine tested in the last 5 years.

Though some entries here may list MPGe figures—these "mpg equivalent" numbers apply only to plug-in hybrids.

## Techstack used in this project

| Tool                     | Purpose                            | Why I use it                                             |
| ------------------------ | ---------------------------------- | -------------------------------------------------------- |
| **VS Code**              | Main IDE                           | Write/run Python and manage all project file             |
| **Python**               | Scraping + cleaning + calculations | Automates collecting and preparing hundreds of tests     |
| **Requests**             | Download web pages                 | Simple free Python library for HTTP requests             |
| **BeautifulSoup**        | Read webpage HTML                  | Helps extract data i.e. vehicle name and tested FE       |  
| **Pandas**               | Clean/transform data               | Easier than manually processing rows and columns         |
| **NumPy**                | Numerical support                  | Useful for calculations; Pandas uses it underneath       |
| **SQL Server + SSMS**    | Permanent structured storage       | A database layer                                         |
| **SQLAlchemy / pyodbc**  | Python for SQL Server connection   | Let Python insert cleaned data into SQL Server           |
| **Power BI Desktop**     | Dashboard and visualization        | I'm on Windows                                           |
| **Git + GitHub Desktop** | Version control                    | Track changes and publish this project                   |
| **GitHub**               | Public portfolio repository        | Shows project documentations                             |

## Data Source Information

I chose Car and Driver because it's a print and digital magazine covering the newest car offeringsand helping people shopping for a car by serving up unique brand of intelligence, independence, and irreverence in magazine business since 1955 and online for more than two decades and I found the review balances the subjective with objective data.

## How Car and Driver tests Fuel Economy and Driving Range from their cars

**Source : https://www.caranddriver.com/features/a32018270/how-we-test-cars/**

All light-duty vehicles are required by law to have their fuel-economy estimates certified by the U.S. Environmental Protection Agency (EPA). These city, highway, and combined ratings are boldly listed on new vehicles' window stickers and often used by manufacturers as advertisement fodder. Plug-in hybrids and electric vehicles also receive estimates for electric operation. Expressed in MPGe, these estimates are intended to be an easy way to compare the efficiency of an electric to a gasoline-powered car on an energy-equivalent basis. But there is a drawback to using EPA numbers that few people realize: the agency actually does very few of its own tests. 

The EPA lists ratings that are mostly self-reported by auto manufacturers. Whether the testing is performed by the automaker or the EPA, they are done inside on a sort-of treadmill for vehicles that eliminates variables such as temperature and traffic. These scientific methods provide the best way to directly compare two vehicles. However, the EPA tests are not necessarily indicative of how people drive in the real world, and the test cycles don't include speeds as low as what's experienced in areas of dense traffic or high as those that tend to be driven on U.S. highways.

### Highway Fuel-Economy Test

We run all our tests at a GPS-verified 75 mph on a 200-mile out-and-back loop on the highways that surround our Michigan headquarters. Our consistent procedure includes a methodical fill-up process, following a specific route, using cruise control, and setting the climate control to the same temperature (72 degrees auto). We also correct for odometer error, and we don't test in heavy wind or rain or with extra passengers. In the event we encounter too much traffic or unusual conditions, we abort the run and try again later.

We follow the same procedure for electric vehicles and plug-in hybrids, except for these, we have additional steps that include making sure the battery is fully charged before starting and recording the battery state of charge and predicted range values every five miles, and then the kilowatt-hours (kWh) needed to fill the battery after the drive loop. Plug-in hybrids also get a highway EV range and MPGe economy for those miles. MPGe is calculated just like miles per gallon of gas only using the EPA's equivalence factor of 1 gallon = 33.7 kWh of electricity to arrive at the result. For plug-ins that can't hit 75 mph in electric mode, we instead first drain the battery and then start the test in charge-sustaining (hybrid) mode. Since those plug-ins don't use any electricity, their results are in miles per gallon rather than MPGe. Likewise, we have to shorten our route for EVs that don't have the range to complete the entire loop. We still give them an MPGe number, though.

### Highway Driving Range

The highway range figure we report is the maximum distance that a vehicle can travel at 75 mph on a full tank of gas. We take the fuel economy from our highway test and multiply it by the vehicle's fuel-tank capacity. For example, the six-cylinder Mazda CX-90 averaged 30 mpg on our fuel loop and has a 19.6-gallon tank. This equates to an impressive 588 miles of range, but we round down to the nearest 10-mile increment and publish it as 580 miles. That's because when it comes to something that can strand you by the side of the road, we believe it's better to publish conservative figures rather than distances that are more difficult to achieve. A range figure under about 400 miles is the threshold where fill ups can become annoyingly frequent.

Our process is different for electric vehicles and plug-in hybrids. For plug-ins, we simply note how many miles we get into our loop before the battery runs out of juice and the vehicle switches on the internal-combustion engine. EVs are more complicated, because as the battery charge gets really low they generally can't maintain highway speed and tend to go into a low-speed limp mode. (Plus, then we'd be stranded on the side of the highway.) And we also can't calculate range based on the energy put back into the pack after a test, because that would include the inefficiencies of the charging process. So we use our log of estimated range and battery state of charge from the trip computer every five miles. We then plot all of those points and fit a curve to project out to our range figure, again rounding down to the nearest 10-mile increment.
Advertisement - Continue Reading Below

### Observed Fuel Economy

To give consumers an idea of how efficient a vehicle is in mixed driving conditions, we track all fill-ups and mileage on our test vehicles. We do the same with electric vehicles and plug-in hybrids, except for those we track electrical energy (kWh) instead of gallons of fuel. This information is documented for every model that is part of a comparison, long-term, or instrumented test. However, we eliminate the miles recorded during track testing and during our highway fuel loop. We also ensure that every odometer reading is accurate to create a level playing field for all the cars we test.

The observed fuel-economy number we publish has variables such as driving style (our staffers have heavier feet than most consumers, and some more than others) and distance traveled. This means that comparing the economy of one tested vehicle to another can be imperfect except for in our comparison tests, for which all the cars are driven the same distances and in the same conditions. So we consider our observed mpg as supplementary to the EPA estimates and the results of our real-world highway fuel-economy test.