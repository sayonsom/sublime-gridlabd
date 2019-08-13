# Build GridLAB-D Models Faster with `sublime-gridlabd`

A Sublime Text 3 snippet collection to supercharge electric feeder modeling with GridLAB-D

### How to use?
To build a feeder with three customers and one customer with solar rooftop, as shown in the graphic below:

here's all you the keystrokes you have to make:  

glm_feeder_template
Transformer
voltage_regulator
Node
Node
Node
Node
Node
oh_line
oh_line
oh_line
oh_line
Add_customer
Add_customer
Add_customer
Add_customer_with_pv
player
measurements

16 lines of typing to generate XXXX lines of code. I would call that XX.XX % efficiency improvement. In terms of time, it took me 4 minutes to build the model, compared to 2.5 hours the first time I built it using the naive method. Here's a list of `sublime-gridlabd` shortcodes. 

###  Installing `Sublime_GridLABD`

Feel free to build your own model using the shortcodes above. 

###  What about other editors?
In 2016, an open-source language support for GridLAB-D was published for Atom. However, it doesn't have the ease of building models that `sublime-gridlabd` has. Also, h 
 
### Understanding the intent and the limitations

`sublime-gridlabd` is very effecient for building new models - especially, small, experimental ones, or for adding on top of huge feeder models. It does not replace any conversion-based workflows people use with GridLAB-D. Also, this is not intended to simplify the GridLAB-D learning curve, but, make development faster for those who are already well-versed with GridLAB-D. 


### More about `sublime-gridlabd`

#### Blogs

This post was first published in thesmartgrid.com and re-posted in Medium. 

#### Video Tutorial



