![alt text](pycloudformer/static/logo.png "PyCloudFormer Logo" ) 

---
### Cloud Formation Program that Generates AWS CloudFormation scripts in YAML

The project is still under development. However, the goal is to have a tool that can easily generate dynamic CloudFormation
Scripts. 

The benefit would be creating these scripts without the need to worry about the YAML indenting, structure and
other requirements that AWS demands. All the user will need to do is add and remove simplistic parameters in one YAML file.
This will result in the production of one or more CloudFormation YAML scripts that are easily scalable, modify-able and
super easy to read and understand.


#### Application Specs
PyCloudFormer makes use of vanilla Python, Jinja2 and YAML for easy-to-read CloudFormation Script creation.
The configurations beyond the dynamic YAML and Jinja2 files would ideally be simplistic.

![alt text](pycloudformer/static/python.png "Python Logo" ) ![alt text](pycloudformer/static/yaml.png "Yaml Logo" ) 

For now the user would interact with:
* YAML Configurations: pycloudformer/configs/StaticServices.yaml
* Python Application: pycloudformer/app.py

By simply adding and removing configurations in the YAML file, the user can run the app.py application which 
will output CloudFormation scripts that are ready to use in the output file - pycloudformer/output.

This interface with the application will be refined over time as the templating and dynamic scripting is completed.

#### Keeping up to date with AWS
As most AWS users will know, the services are constantly under rapid development. Changes and improvements will me
introduced almost daily. 

![alt text](pycloudformer/static/aws.png "AWS Logo" )

I work on this project in my spare time, and would like to refine and write better code and
also produce the most current CloudFormation scripts in the application. However, patience with the project is 
expected. Please feel free to add any comments or suggestions.

#### Progress
To see details on the project and what is currently happening in the development stages have a look:
* [Project Kanban](https://github.com/DirksCGM/PyCloudFormer/projects/1)
* [Development Wiki](https://github.com/DirksCGM/PyCloudFormer/wiki/PyCloudFormer-Development-Journal)

## PyCloudFormer now supports:
* Static AWS Glue Services
    * Glue Jobs
    * Glue Classifier
    * Glue Database
    * Glue Crawler
    * more will be added...
* More Services will be added...