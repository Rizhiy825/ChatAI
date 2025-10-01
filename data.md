# How to use Single Sided Connectors?
Sometimes you might need to place connectors without anything to connect to вЂ“ single sided. In this example we want to use a door as a fixed panel in the front.

First, create your own design without the door.

Before you can attach the door, you will have to position the dowels. SmartWOP usually wonвЂ™t allow placement of single sided connectors, unless you activate Allow single sided connectors in the top right corner of the Machinings tab.

---

# Converting Bores to Pockets in SmartWOP
There may be cases where you donвЂ™t want to drill a hole in your panels but rather treat them as a small pockets and have them milled.

In order to do this within SmartWOP follow this short guide.

Go to File>Options>Workshop here you can find the new settings in the lower right corner.

Now you need to enter the drill diameter in mm followed by => and the Tool Number you want to use for your pocket.

Example: 10=>201;12=>201

After you have saved your settings, restart SmartWOP and the diameters you have entered will now be treated as pockets.

---

# Using woodWOP components in your project
To use a woodWOP component in your SmartWOP project navigate to the Machinings tab. Click on woodWOP Component in the Free Machinings section.

Now the properties window for this special machining type opens.

By default the file is named external.mpr this comes preinstalled with SmartWOP and is ready to be used and edited.  To create a new woodWOP component, change the file name or select an existing woodWOP component using the icon with the three dots to browse your computer.

Clicking on the woodWOP icon starts woodWOP. You can only edit components in woodWOP if you have previously unchecked the вЂњEmbeddedвЂќ option.

In woodWOP you can now edit the component to fit your needs and save. The use of variables within the component is highly recommended.

Close woodWOP and return to SmartWOP.

Note: The file is saved in the woodWOP default folder for components. Usually this would be the folder вЂњML4вЂќ within the woodWOP directory.

You can now drag the machining type woodWOP component onto a part of your design.

Your component is represented with a wireframe cube, clicking on it will open the preferences.

You can access and edit the parameters you implemented in woodWOP in the Parameters section.

The arrows can be used to swap to different reference points. Note the axis indicators in red and green to help.

You can now also decide to embed the component in the file and set conditions from woodWOP.

---

# Creating connector variants
SmartWOP comes with a selection of preinstalled connector types that are most commonly used. But you can always create more. This guide will give you an example of how to create a new connector.

In this guide we will take a look at the Screws and create a new type

Go to the Machining tab (Hotkey: B) and find the Screws icon and click it.

The Screws template will open. (Templates have a red area on the left while preferences of already placed connectors have none)

In the Fitting section, you can enter the name of your new screw as well as Supplier and Article numbers, and while the name is mandatory to differentiate the screws, supplier and article number are optional.

Now it is time to define the Screw by defining the drilling diameters.

Diameter 1 is the boring diameter for the first panel the screw will pass through and Diameter 2 for the second panel, see the extreme example underneath for reference. Lenght is the lenght of the bore.

Once you are happy with your new screw dimenstions and name you can start using it right away, or hit the Floppy Disk icon to save the template (meaning all of the settings including screw count and distances will be applied the next time you use this connector) The screw itself has already been saved and can be selected from the Fitting list.

It is possible, that you are not the only person working with SmartWOP in your company, and that the other guy keeps on messing up your connectors вЂ“ so you have to readjust them every time. 

Prevent him from doing that by creating connectors in Administrator Mode.

Go to File>Options>General and check the box for Administrator Mode and confirm by clicking on Apply. Now return to the Machining tab. Create another new Screw. Upon hitting Enter in the Fitting name section, you will notice an open lock icon.

This indicates that you have the right to change the screwвЂ™s parameters. Once you are done, either restart SmartWOP or exit the Administrator Mode by unchecking its box.

When you look at the screw now, you will notice a closed lock. 

This means, that if someone tries to change the parameters of this screw now, SmartWOP will not allow it, instead it will create a copy of it -indicated by the *.

Your screw however can always been selected from the dropdown now, without any changes to them.

Please note, at this point it is not possible to have screws you created in the Screw connector category appear in the list for Screws/Dowels and the other way around. You have to create it separately for each connector type. 

---

# Traverses/Cross Beams and Separators
When using Traverses/cross beams in your build, panels that you want to go underneath the cross beam will be placed with a setback. That is not always wanted, here is how you prevent that.

In this example the cross beam was placed flush in the top part of the design.

If a Horizontal Panel is dragged in underneath the traverse it has a setback equivalent to the thickness of the traverse.

To prevent this from happening you need to use a Horizontal Separator вЂ“ and you need to place it first, before the cross beam.

Drag the Horizontal Separator into your carcass, and position it in a distance equivalent to the traverse width. 

Now drag in your Frontal Traverse, select either Only Top or Only Bottom from the Type section to get a singular beam and adjust size if necessary.

Every Horizontal Panel dragged in underneath the traverse now will be using the whole volume inside the carcass.

Hint: This will work with Horizontal Traverses and Vertical Separators accordingly. 

---

# Installing rebated back panels.
Depending on your building style you might need to change how the back panel is installed in your design. Here is how you can insert a thick rebated back panel.

This is the Back Panel Template.

It allows you to change its basic values such as Thickness and Setback. It is important to know, that a setback of 20 mm and a Back Panel of 8 mm means the actual Setback is 12 mm.

Overlap determines how far into your carcass panels the back panel will insert.

Back Panel Rebating is most helpful for thicker back panels. Front and Back will determine the distances highlighted below.

Air Gap Width determines a gap around the rebate for easier installation.

Unselecting Machine on CNC prevents SmartWOP from writing a program for the back panel. If it is selected however, you will need to determine a Tool Number in the dropdown menu which you can use with a Custom Feedrate too.

---

# Construction with SmartWOP вЂ“ The first cabinet
Get a Base Volume вЂ“ SmartWOP construction is based on volumes, so for you to start working on your own design you need a Base

Base volumes can be found in the Items tab (Hotkey: E). For this guide we will use a regular base. Drag the volume into your work area on screen.

When you have dragged the base into the work area a window with its properties will open. Here you can name the Base, which is important, because every program and list item will be named accordingly.

Here you have to define the dimensions of the base вЂ“ you can change them at any time and everything you have constructed inside the base will adjust accordingly.

Once you are happy with your dimensions. Click on the Export section of the base template. Especially when you are just starting to use SmartWOP you need to set this up the way you prefer to work on your CNC center.

---

# Mouldings, Cover Panels and Infills
To demonstrate the way Infills/Cover Panels/Mouldings work in SmartWOP we will use this design as an example:

This design consists of two base volumes. The task is to connect them together. A worktop is needed on top of the two carcasses and we have an infill panel on the bottom.

This is the starting situation. We will start with the Cover Panel for the top.

Holding CRTL down click on both top panels of these two bases.

While they are highlighted, simply drag a Cover Panel on top.

In the example the worktop is extending over the front and sides by 50 mm. Click on the Cover Panel to bring up its properties.

Now simply change the values accordingly. Left, right and front got a +50 in this case.

For the Infill on the bottom it is the same procedure.

Select both bottoms using CRTL while you click.

While the bottoms are highlighted, drag an Infill onto them.

---