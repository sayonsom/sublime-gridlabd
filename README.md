# Build GridLAB-D Models Faster with `sublime-gridlabd`

![](example_built_models/figs/sublime-gridlabd-logo.PNG?raw=True)

A Sublime Text 3 snippet and model templates collection to supercharge electric feeder modeling with GridLAB-D. 

### Why do you need it?

- GridLAB-D has no GUI
- Developing new models is labor-intensive and error-prone 
- Lots of documentations to consult.

### Installation

Since `sublime-gridlabd` is just a bunch of files, it can be downloaded on any computer that has Sublime Text, and files can be extracted to the correct folder:

Here are some common installation work-flows:

#### Windows 

- Open any folder window and use the address bar to go to `%APPDATA%\Sublime Text 3`
- Get the path from the directory that opens up
- Download this repository as a ZIP file, and extract it to the directory we got to in the last step

#### macOS

- Open this folder: `~/Library/Application Support/Sublime Text 3`
- Download this repository as a ZIP file, and extract it to the above folder

#### Linux (Ubuntu)

- Open this folder: `~/.config/sublime-text-3`
- Download this repository as a ZIP file, and extract it to the above folder (If unzip is not installed, `sudo apt install unzip`)


### List of Shortcodes 

_Alphabetically_: 

- `add_house_this_xmfr` : Add a customer house in the same secondary distribution system. The customer house has a default ZIP load
- `add_house_with_pv_this_xmfr` : Add a customer house template in the same secondary distribution system, and this customer has a solar PV installation in their house. 
- `add_solar` : Add a solar PV installation template to an existing house/customer node
- `capacitor` : Install a capacitor
- `feeder_template` : Create a template for developing a boiler-plate feeder model. This has default configurations for overhead, underground, triplex lines, transformers, and regulators. To create new configurations, the user can create
- `house`: Add a house with a default ZIP load. The house can be replaced be replaced by a typical American house with appliances using the following command. 
- `house_detail`: Creates a typical American household with appliances such as dishwasher, washer-dryer, microwave ovens, etc.  
- `load` : Add a three-phase load template to the model
- `meter` : Add a meter template to the model
- `multi_recorder` : A template for recording multiple measurements in a single file, based on `tape` module
- `new_branch` : Creates a secondary distribution system branch, with one distribution transformer and customer
- `new_branch_with_pv` : Creates a secondary distribution system branch, with one distribution transformer and customer, and this customer has a solar PV installed. Please remember that every model that has a solar PV installation will need a climate file. If you are developing using the `feeder_template` short-code, please remember to uncomment the climate object and module towards top of the file.  There are some climate files (TMY3 format, do not use TMY2 as it does not deal with Daylight Savings Time) in the resources/climate_files directory of this repository, else you can download by ZIP Code from [this NREL Website](https://rredc.nrel.gov/solar/old_data/nsrdb/1991-2005/tmy3/by_state_and_city.html). 
- `node` : Adds a new node object to the model
- `oh_line` : Adds a new overhead line to the model, based on default configuration. 
- `player` : Adds a player object template to pass to other objects, for varying properties of those objects w.r.t time.
- `recorder` : Adds a recorder object template to record measurements of various properties 
- `regulator` : Adds a regulator object template 
- `substation` : Adds a substation template, to create downstream feeders
- `switch` : Adds a switch template to the model. This is an edge (or a link) that connects to different nodes
- `transformer` : Adds a transformer template, with default transformer configuration, as created by the `feeder_template` shortcode
- `triplex_line` : Add a customer connection template, default split-phase is AS
- `triplex_node` : Add a triplex node, to which other residential customers can be connected
- `ug_line` : Adds a new underground line to the model, based on default configuration. 


### Building a simulation model demonstration

#### Example 1: One Node Test System

Let's build a simple model to see how much money one can save by improving the insulation of their homes. GridLAB-D can help us with these kind of simulations. We'll build a simple one-house model:

![Simple Feeder with One House](example_built_models/figs/simple_feeder_1_house.png?raw=True "Simple Feeder with One House")

Here is the sequence of shortcodes you need to write in your Sublime Text 3 to generate the GridLAB-D model:

```
node
node
node
oh_line
oh_line
oh_line
new_branch
multi_recorder
```

Now, after the model is built, you can go to the terminal, navigate to the directory where the code is, and then: 

```
gridlabd simple_feeder.glm
```

A CSV file ("simple_feeder_records.csv") with the simulation results are generated. Since there is one house, you can start by playing around with the thermal integrity of the house inside the house code block. Here's a plot on the customer's energy consumption at the end of the day and how much he/she has to pay to the utility.

![Billing Costs and Energy Consumption Simulation](example_built_models/figs/simple_feeder_1_house_results.png?raw=True "Simple Feeder with One House")


#### Did you notice the efficiency boost? 

> 7 lines of code to generate 265 lines of code. I would call that 99% efficiency improvement. In terms of time, it took me 2 minutes to build the model, compared to 1 hour the first time I built it using the naive method. 

Let's try building something a little more complex and realistic below. 

#### Example 2: Simple Smart Feeder Test System (S2FTS)

![Simple Unbalanced Feeder Test System](example_built_models/figs/sufts.png?raw=True "S2FTS Schematic Diagram")

Follow along this Youtube video tutorial, or download the paper for the all the data. (If you use this model in your research, please consider citing it. Here are some common citation formats: Bibtex, IEEE Format. 

You can download the code (i.e. GridLAB-D model) for the S2FTS model in the 'example_built_models' sub-directory of this repository. 


###  Road map and other editors?
In 2016, an open-source [language support for GridLAB-D](https://github.com/nicorikken/language-glm) was published for Atom. However, it doesn't have the ease of building models that `sublime-gridlabd` has. Also, Atom is inefficient for handling a large-sized GLM file, where Sublime Text has a natural advantage. That is why I thought building a developer pack for Sublime would suffice. If there's sufficient interest, I will roll out similar GridLAB-D development packages for other editors (VIM, VSCode, etc).  

### Understanding the intent and the limitations

`sublime-gridlabd` is very efficient for building new models - especially, small, experimental ones, or for adding on top of huge feeder models. It does not replace any conversion-based work-flows people use with GridLAB-D. Also, this is not intended to simplify the GridLAB-D learning curve, but, make development faster for those who are already well-versed with GridLAB-D. 


### Tip Jar

If sublime-gridlabd helps reduce time modeling and development time for you, please 
[consider funding The Smart Grid Project](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RHSC6DAKVML9W&source=url) :)


#### Featured

This post was first published in [thesmartgrid.us](http://thesmartgrid.us) and re-posted in Medium. 





