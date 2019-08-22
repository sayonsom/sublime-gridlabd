# Build GridLAB-D Models Faster with `sublime-gridlabd`

![](example_built_models/figs/sublime-gridlabd-logo.PNG?raw=True)

A Sublime Text 3 snippet and model templates collection to supercharge electric feeder modeling with GridLAB-D. 

### Why do you need it?

- GridLAB-D has no GUI
- Developing new models is labor-intensive and error-prone 
- Lots of documentations to consult.

### Installation

Since sublime-gridlabd is just a bunch of files, it can be downloaded on any computer that has Sublime Text, and filex can be extracted to the correct folder:

Here can be some common installation workflows:

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

- `add_house_this_xmfr` : Add a customer house in the same secondary distribution system
- `add_house_with_pv_this_xmfr` : Add a customer house template in the same secondary distribution system, and this customer has a solar PV installation in their house. 
- `add_solar` : Add a solar PV installation template to an existing house/customer node
- `capacitor` : Install a capacitor
- `feeder_template` : Create a template for developing a boiler-plate feeder model. This has default configurations for overhead, ungergroud, triplex lines, transformers, and regulators. To create new configurations, the user can create 
- `load` : Add a three-phase load template to the model
- `meter` : Add a meter template to the model
- `multi_recorder` : A template for recording multiple measurements in a single file, based on `tape` module
- `new_branch` : Creates a secondary distribution system branch, with one distribution transformer and customer
- `new_branch_with_pv` : Creates a secondary distribution system branch, with one distribution transformer and customer, and this customer has a solar PV installed
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
Let's build a Simple Unbalanced Feeder Test System (SUFTS), as shown in the figure below:

![Simple Unbalanced Feeder Test System](example_built_models/figs/sufts.png?raw=True "Simple Unbalanced Feeder Test System")

Here's a rundown of the keystrokes you have to make (and off course provide the correct parameters).

```
feeder_template
```
Go to the "Nodes" section of the template that just got created:

```
node
node
node

add_house_this_xmfr
add_house_this_xmfr

recorder
```

You can download the code (i.e. GridLAB-D model) for the SUFTS model here. 

#### Did you notice an efficiency boost? 

16 lines of typing to generate XXXX lines of code. I would call that XX.XX % efficiency improvement. In terms of time, it took me 4 minutes to build the model, compared to 2.5 hours the first time I built it using the naive method. Here's a list of `sublime-gridlabd` shortcodes. 

###  Installing `Sublime_GridLABD`

Feel free to build your own model using the shortcodes above. 

###  Roadmap and other editors?
In 2016, an open-source [language support for GridLAB-D](https://github.com/nicorikken/language-glm) was published for Atom. However, it doesn't have the ease of building models that `sublime-gridlabd` has. Also, Atom is inefficient for handling a large-sized GLM file, where Sublime Text has a natural advantage. That is why I thought building a developer pack for Sublime would suffice. If there's sufficient interest, I will rollout similar GridLAB-D development packages for other editors (VIM, VSCode, etc).  
 
### Understanding the intent and the limitations

`sublime-gridlabd` is very effecient for building new models - especially, small, experimental ones, or for adding on top of huge feeder models. It does not replace any conversion-based workflows people use with GridLAB-D. Also, this is not intended to simplify the GridLAB-D learning curve, but, make development faster for those who are already well-versed with GridLAB-D. 


### Tip Jar

If this project help you reduce time to develop, please 
[buy me a cup of coffee](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RHSC6DAKVML9W&source=url) :)


#### Featured

This post was first published in [thesmartgrid.us](http://thesmartgrid.us) and re-posted in Medium. 





