# DevOps_Project2

## Random holiday generator

## Author
### Inaam Islam

### Links
- [Trello](https://trello.com/b/kFb089Jf/random-holiday-generator-start)
- [Risk Assessment](https://docs.google.com/spreadsheets/d/14yRvZVZBuPhvAV8yGtDGZbKzVS5RcJnY/edit#gid=1358709700)

## Contents
- [Brief](#brief)
    - [Requirements](#reqs)
    - [My Approach](#approach)
- [Testing](#test_)
    - [Service 1 test](#test_1)
    - [Service 2 & 3 test](#test_2/3)
    - [Service 4 test](#test_4)
- [Architecture](#arch)
    - [Container level architecture](#cla)
    - [Service-Orientated architecture](#soa) 
    - [Application Infrastructure](#appinf)
    - [Entity Relationship Diagram](#erd)
- [Continuous Integration pipeline](#ci)
    - [CI pipeline - version 1](#ci1)
    - [CI pipeline - version 2](#ci2)

- [Risk Assessment](#risks)
- [Project Planning & Tracking](#use_case)
- [Technologies used](#tech)
- [Successes](#suc)
- [Future Improvements](#improve)

<a name="brief"></a>
## Brief

The brief for the DevOps core practical project was to create a microservice application that would generate "objects" upon a set of predefined rules.

This project will involve concepts from previous training modules, including:

-Software Development with Python
-Continuous Integration
-Cloud Fundamentals

<a name="reqs"></a>
### Requirements 

The requirements of the project were as follows:

The requirements set for the project are below.
Note that these are a minimum set of requirements and can be added onto during the duration of the project.

The requirements of the project are as follows:

-An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
This could also provide a record of any issues or risks that you faced creating your project.
-An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
-If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
-The project must follow the Service-oriented architecture that has been asked for.
-The project must be deployed using containerisation and an orchestration tool.
-As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
-The project must make use of a reverse proxy to make your application accessible to the user.

<a name="approach"></a>
### My Approach
In order to fulfill the requirements of the project I chose to configure a microservice application that would allow services generating random information to communicate and influence the outcomes in other servers. I had a number of diffrent ideas, but eventually settled with creating a Random Holiday Generator. 

#### Service 1
**Service 1** is the Main service. Service 1 communicates with service 2, 3 and 4 and presists data to a MySQL database. The main service will perform a  **GET request on Service 2 and Service 3** and a **POST request on Service 4**. The responses attained from service 2, service 3 & service 4 are used by service 1 to display information to the user via HTML and Jinja2 templating. Furthermore, I configured the databse to allow the user to see the last three holidays that were genearted via a query to the database. 

**routes located:  service1/application/routes.py**
```bash
@app.route('/', methods=['GET','POST'])
def index():
    #get the name of the city 
    city = requests.get("http://service_2_api:5001/city")
    #get the activty 
    activity = requests.get("http://service_3_api:5002/activity")
    price_network = str(city.text) + " " + str(activity.text) 
    price = requests.post("http://service_4_api:5003/price", data=price_network)
    last_3_holidays = holiday_plan.query.order_by(desc(holiday_plan.id)).limit(3).all()
    db.session.add(
      holiday_plan(
          city = city.text,
          activity = activity.text,
          price = price.text
      )
    )
    db.session.commit()
    return render_template('index.html', title='Holiday Generator', 
    city = city.text, 
    activity=activity.text, price = price.text, 
    price_network=price_network, 
    last_3_holidays=last_3_holidays)
```
A generator button was included in the HTML file to allow users to generate a random holiday. 

**routes located:  service1/application/templates/index.html**
```bash
<a href="{{ url_for('index')}}"><button>Generate</button></a>
```
#### Service 2

This service generates a random city. There are 4 possible cities that can be generated.


**routes located:  service2/application/routes.py**


