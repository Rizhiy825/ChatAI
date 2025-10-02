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

# Insert base
Select a base from items in the lower right corner. Pull the base with the left mouse button pressed into the construction level

---

# Move bases
Left‑click the base you want to move. Hold the left mouse button pressed on the arrow in the direction you want to move the base and release the left mouse button when you have reached the desired position

---

# Rotate bases
Left‑click the base you want to rotate and select the rotation button in the menu bar. The rotate button turns blue while you are in rotation mode. In the submenu of the rotation button select the desired degree of rotation. The axis arrows turn into circles: hold down the left mouse button on a circle and move the mouse to rotate the base. Leave the rotation mode by left‑clicking the rotation button again

---

# Clone bases
Left‑click the volume you want to duplicate and select the duplicate button on the menu bar. The volume will be duplicated with all its contents. In the drop‑down menu you can choose to mirror the selected base

---

# Overlapping bases
Select the Allow Overlapping button in the start bar. Drag the volume as described in “Move bases” to the desired position using the arrows. The allow overlapping button remains blue while you are in this mode. After switching off allow overlapping it is no longer possible to move bases into each other

---

# Select bases
Select the base button in the start bar and choose the desired base with a simple left click. To select several bases at the same time hold down the Control key (CTRL) and select each base with a single left click

---

# Activate bases
After selecting one or several base volumes you can activate them by clicking the Activate volume button. SmartWOP allows you to edit only the green‑marked bases. You can also select a panel and click Activate volume to activate the base to which the panel belongs, which is helpful when working with many separators

---

# Change base dimensions
Double‑click the base whose dimensions you want to change. Each side will display a corresponding arrow which you can drag with the left mouse button to change the base dimensions. Alternatively, use the input fields at the arrows or dimension lines to enter the desired dimensions

---

# Base settings
When you select a base the settings window opens. Here you can change the name of the base and select its type. Choosing a Construction kit allows items within the volume to be output to the superordinate volume when saving the volume as a component, while choosing Cabinet outputs items within the base to the base itself when saving the volume. Selecting Article outputs the items within the base as purchased parts with an article number when saving the volume; components of a volume specified as an article are not output as parts to be produced. You can change the base’s width, height and depth (including using formulas) and enter a description that is only visible in this window. The Count field specifies how many bases to produce; the number of bases appears in the material list. You can select an export reference point (front or back) to determine orientation on the machine. Under Accessories double‑click to open a submenu for adding accessories; items will appear in the purchase list. Under Transformation you can set offset and rotation values for X, Y, Z

---

# Back Angled Base
In the base settings window of a back‑angled base you can enter values for front height, back height, top depth, bottom depth, angle and safety clearance. Dimensions that are not entered will be calculated and added by SmartWOP automatically. The angle corresponds to the angle in the horizontal (0°–90°), and the safety clearance defines the space between the base and the cabinet

---

# Slanted Base
In the base settings window of a slanted base you can enter height left, height right, width top, width bottom and angle. Dimensions that are not entered will be calculated automatically. The angle corresponds to the angle in the horizontal. To get the angle on the right side of the base enter a negative angle (‑0° to ‑90°); to get the angle on the left side enter a positive angle (0°–90°)

---

# Corner Slanted Base
In the base settings window of a corner slanted base you can enter back width, left width, front depth and right depth. The opening angle will be calculated and added automatically by SmartWOP

---

# Roof Window
In the base settings window of a roof window you can enter several settings: window width, window height, window depth, total installation depth, material thickness, roof angle, left angle and right angle. You can also enter the desired frame dimensions (depth and width) for the window and wall connection

---

# Insert Separators
Before you can insert items you need a base. Drag and drop separators into the base. Work from the outside towards the inside in SmartWOP. Separators that you insert will split the base without adding panels and are required for complex constructions. If you construct panels calculated on separators you cannot delete the separator without deleting the panel. Separators used to separate panels can be linked together by selecting the panels and right‑clicking to choose link in the dropdown menu

---

# Horizontal Separator
Drag the horizontal separator into the base. You can drag the separator by arrows into position or enter the desired dimensions. In the settings window you will find more options to optimise your separator. The Absolute Position setting determines the space of your separator relative to the base outline; the arrow on the right side of the row allows you to switch between top or bottom base outside line

---

# Vertical Separator
Drag the vertical separator into the base. You can drag the separator by arrows into position or enter the desired dimensions. In the settings window you will find more options to optimise your separator. The Absolute Position setting determines the space of your separator relative to the base outline; the arrow on the right side of the row allows you to switch between left and right base outside line. SmartWOP displays the height of the separator

---

# Frontal Separator
Drag the frontal separator into the base. You can drag the separator by arrows into position or enter the desired dimensions. In the settings window you will find more options to optimise your separator. Use Absolute Position to determine the space of your separator relative to the base outline; the arrow on the right side of the row allows you to switch between front and back base outside line

---

# Diagonal Separator X
Drag the diagonal separator X into the base. You can drag the separator by arrows into position or enter the desired dimensions. In the settings window you will find more options to optimise your separator. Use Absolute Left Position and Absolute Right Position to determine the space of your separator relative to the base outline; the arrows on the right side of the rows allow you to switch between top and bottom base outside line. Enter the desired angle (‑89° to 89°) and a safety clearance to determine how much space you want between other diagonal separators

---

# Diagonal Separator Y
Drag the diagonal separator Y into the base. You can drag the separator by arrows into position or enter the desired dimensions. In the settings window you will find more options to optimise your separator. Use Absolute Front Position and Absolute Back Position to determine the space of your separator relative to the base outline. Enter the desired angle (‑89° to 89°) and a safety clearance to determine how much space you want between other diagonal separators

---

# Diagonal Separator Z
Drag the diagonal separator Z into the base. You can drag the separator by arrows into position or enter the desired dimensions. In the settings window you will find more options to optimise your separator. Use Absolute Left Position and Absolute Right Position to determine the space of your separator relative to the base outline; the arrows allow you to switch between front and back base outside lines. Enter the desired angle (‑89° to 89°) and specify the orientation of the diagonal separator Z to bring it into the desired position

---

# Universal Separator
Drag the universal separator into the base. You can drag the separator by arrows into position or enter the desired dimensions. In the settings window you will find more options to optimise your separator. You can specify the centre position and rotation of the separator in X/Y/Z

---

# Insert Items
Before you can insert items you need a base. Insert items into your base by drag and drop. Remember that you work from the outside to the inside in SmartWOP

---

# Horizontal Panel
The horizontal panel can be used as a bottom panel, top panel or construction panel. Drag the horizontal panel into the base and position it using arrows or by entering dimensions. In the settings window you will find more settings to optimise your panel

---

# Vertical Panel
Drag the vertical panel into the base and position it using arrows or by entering dimensions. In the settings window you will find more settings to optimise your panel. Use the Absolute Position setting to determine the space of your panel relative to the base outline; the arrow on the right allows you to switch between right or left base outside line. Enter a setback to reduce the volume for subsequent items, specify how many panels you need, define the distance between panels and set the thickness. You can extend the panel over the base volume but cannot add panels outside the base volume

---

# Frontal Panel
Drag the frontal panel into the base and position it using arrows or by entering dimensions. In the settings window you will find more settings to optimise your panel. Enter a name, determine the space of your panel relative to the base outline, specify thickness and adjust panel dimensions as needed. You can extend the panel over the base volume but cannot add panels outside the base volume

---

# Back Panel
Drag the back panel into the base and enter the desired dimensions. In the settings window you will find more settings to optimise your panel. You can enter a setback, thickness and overlap for each side. Panels can be extended over the base volume, but you cannot add panels outside the base volume. Additional options include back panel rebating, milling depth on the front or back side, machining on CNC and custom feed rates. You can define air gaps and groove extensions for each side

---

# Horizontal Traverse
Drag the horizontal traverse into the base. Position it by arrows or by entering dimensions. In the settings window you will find more settings to optimise your panel, such as name, absolute position, width, thickness, execution type (between two panels, only front panel or only back panel), front and back setbacks, and options for skewed edges and pick point

---

# Frontal Traverse
Drag the frontal traverse into the base. Position it by arrows or by entering dimensions. In the settings window you will find more settings to optimise your panel, such as name, absolute position, width, thickness, execution type (between two panels, only front panel or only back panel), top and bottom distance, and options for skewed edges and pick point

---

# Adjustable Shelves
Drag the adjustable shelves into the base and position them using arrows or by entering dimensions. In the settings window you will find more settings to optimise your shelves, including name, skewed edges, count, top and bottom distance, individual shelf positions, distance between shelves, thickness, setback, air gap and pick point

---

# Diagonal Panel X
Drag the diagonal panel X into the base and position it using arrows or by entering dimensions. In the settings window you will find more settings to optimise your panel, such as name, absolute left and right positions, angle (‑89° to 89°), setback, safety clearance, thickness, adjustable panel dimensions, and pick point

---

# Diagonal Panel Y
Drag the diagonal panel Y into the base and position it using arrows or by entering dimensions. In the settings window you will find more settings to optimise your panel, such as name, absolute front and back positions, angle (‑89° to 89°), safety clearance, thickness, skewed edges and pick point

---

# Diagonal Panel Z
Drag the diagonal panel Z into the base and position it using arrows or by entering dimensions. In the settings window you will find more settings to optimise your panel, such as name, absolute left and right positions, angle (‑89° to 89°), thickness, orientation, skewed edges and pick point

---

# Universal Panel
Drag the universal panel into the base. Position it by arrows or by entering the desired dimensions. In the settings window you will find more settings to optimise your panel, including the centre position in X/Y/Z, rotation in X/Y/Z, thickness, orientation, skewed edges and pick point

---

# Drawer Bottom
Drag the drawer bottom into the base and position it using arrows or by entering dimensions. In the settings window you will find more settings to optimise your panel, such as name, distance from the outer bottom baseline, thickness, overlap, carcass rebate extension, air gap width and depth, groove/fold extensions for each side, skewed edges and pick point

---

# Cover Panel
The cover panel can only be placed outside the base. Drag the cover panel onto the base and use the settings window to optimise it. You can enter a name, thickness, individual panel positions, choose whether the panel is on the exterior or interior side and set a pick point

---

# Filler/Infill
The filler/infill can only be placed outside the base. Drag the filler/infill onto the base and use the settings window to optimise it. Enter a name, thickness, width, position setback and distance to the corpus panel. Use the Panel Dimensions dropdown to cut or extend the panel. You can add a mounting panel and specify its dimensions, choose whether the panel is on the exterior or interior side and set a pick point

---

# Enter Doors and Drawer fronts
To insert doors and drawer fronts you need a volume into which they can be inserted. Drag and drop doors and drawer fronts into the volume

---

# Inset Door
Pull the inset door into the volume. In the template window you will find options for optimising your workpiece. You can name the workpiece, specify if it is a double door, enter its thickness, set gaps on each side, choose overlay on the carcass, select a door frame and frame width, define setback, chamfer the outer edges, add dampers and define their position and dimensions, and set a pick point for components or splitting operations

---

# Overlay Door
Pull the overlay door into the volume. In the template window you will find options for optimising your workpiece. You can name the workpiece, specify if it is a double door, enter its thickness, set gaps on each side, choose overlay on the carcass, select a door frame and frame width, define distance and chamfer, add dampers and set their position and dimensions, and set a pick point for components or splitting operations

---

# Framed Door
Drag the framed door into the volume. This type of door stores different door designs that need to remain quickly accessible in recurring constructions and do not require major changes. In the template window you will find options for optimising your workpiece. You can name the workpiece, specify if it is a double door, enter its thickness, set gaps, choose overlay on the carcass, define door frame and frame thickness, set distance and chamfer, add dampers and set their position and dimensions, and set a pick point

---

# Drawer Front
Pull the drawer front into the volume. In the template window you will find options for optimising your workpiece. You can name the workpiece, specify the number of drawer fronts (SmartWOP will automatically divide them evenly), enter individual heights, use fronts as separators or combine them again, set thickness, gaps, overlay, distance and chamfer, add dampers and set their position, and set a pick point for components or splitting operations

---

# Sliding Door
Pull the sliding door into the volume. In the template window you will find options for optimising your workpiece. You can name the workpiece, specify the number of sliding doors (SmartWOP will automatically distribute them evenly), enter thickness, layout (single or double rails), door offset, overlay, overlap and the first door on the first rail, set gaps and distance, choose chamfer, add dampers, and set a pick point for components or splitting operations

---

# New
Use the New button in the Home Bar to start a completely new SmartWOP project in an empty scene

---

# Office Mode

Office mode renumbers items throughout your design during planning. The numbering can change if you add or edit items later, so avoid exporting items until the design is finished. Projects saved in office mode reopen in office mode

---

# Workshop Mode

Workshop mode freezes item numbering so numbers stay fixed for production. Only changed items are renumbered when modifications are made. Switching back to office mode recalculates all item numbers. Projects saved in workshop mode reopen in workshop mode

---

# Delete
Click Delete to remove the selected items from your project

---

# Duplicate
Use Duplicate to copy a complete base volume along with its items. Select an item in the volume or the entire volume, then click Duplicate. It is not possible to duplicate single items

---

# Mirror
Use Mirror to create a mirrored copy of a base volume with its items. Select an item in the volume or the entire volume, click the arrow under Duplicate and choose the mirror option. Individual items cannot be mirrored

---

# Allow Overlapping
Activate Allow Overlapping to temporarily permit volumes to overlap. With this button on, you can move volumes into one another using the arrow handles. Click the button again to deactivate overlaps; overlapping volumes can still be pushed apart without reactivating the button

---

# Rotation
Use Rotation to rotate volumes together with their items. Click the arrow under the button to choose the rotation angle, activate the button, select the volume and drag the circular arrows to rotate around the desired axis. Click the button again to exit rotation mode

---

# Volume
The Volume button lets you select complete volumes. Click it again to switch back to selecting individual items

---

# Activate Volume
Use Activate Volume to restrict editing to a selected volume. After selecting a volume with the Volume button, click Activate Volume; the activated volume is outlined in green and operations outside it are disabled. Click again to release editing for other volumes

---

# Select and Move
Select and Move is the default control mode that allows you to select and move items. It remains active until you activate another tool such as Rotation

---

# Additive Selection
Activate Additive Selection to select multiple items or volumes. You can perform the same action by holding the Ctrl key while clicking items

---

# Subtractive Selection
Activate Subtractive Selection to deselect items or volumes. You can also hold the Alt key while clicking to deselect

---

# Frame
The Frame tool lets you draw a selection rectangle to select several items at once. Only items entirely within the frame are selected

---

# Revert Selection
Click Revert Selection to invert the current selection of elements

---

# Machining
Select Machining to switch to edit mode, where you can add machining operations to items

---

# Hide Fronts
Use Hide Fronts to temporarily hide all fronts so you can more easily select interior items. Remember to show all fronts again before exporting your construction; only visible items are exported

---

# Hide Selection
Use Hide Selection to hide selected items so you can better work on internal parts. Show them again before exporting; only visible items are considered

---

# Hide Unselected
Use Hide Unselected to display only selected items. This helps isolate components for machining or exporting. Before exporting, show all items again

---

# Show All
Click Show All to display all items in the scene. Ensure all items are shown before exporting

---

# Show Separators
Use Show Separators to toggle the visibility of all separators. Hiding separators makes selecting interior items easier; click again to show them

---

# Solid mode
Select Solid mode to switch from transparency to solid material display. The submenu allows you to toggle contour lines in material mode. Click again to return to transparency mode

---

# Activate snapping
Activate activate snapping to set a minimum movement step for items. Enter the minimum distance in millimetres in the field below

---

# Magnet
Activate Magnet to enable automatic magnet points when moving objects. Enter in the field below the distance from which a workpiece should be attracted to a magnet location

---

# Measure
Use the Measure tool to measure distances between points. Activate the button, select a starting point and drag a dimension line to the desired point. If points are on different axes, SmartWOP also displays X/Y/Z values. Measurement displays are temporary and disappear when a new point is selected

---

# Dimensioning
Use Dimensioning to create permanent dimension lines. Activate the button, select a start point and drag to an end point; you can move the dimension display by dragging it. Dimensions remain until you delete them using the delete function

---

# Comment
Activate Comment to add comments to specific items or volumes. Click an item to attach a comment identified by the item name, then enter your text. You can move comments by dragging them. Comments remain until deleted and can be shown or hidden in the View task

---

# Collision
Use Collision to check your project for collisions between machining elements. Colliding points are highlighted in red

---

# Edit Top
Select an item and activate Edit Top to insert machining on the top side via WoodWOP. The side to be machined is marked with a yellow arrow

---

# Edit Bottom
Select an item and activate Edit Bottom to insert machining on the bottom side via WoodWOP. The side to be machined is marked with a yellow arrow

---

# Activate Assistant
Activate Activate Assistant to enable your assistant. In the Assistants menu at the bottom right you can create an assistant to speed up recurring constructions

---

# Export Tuning
Activate the button to open the Export Tuning.
In the Export Tuning submenu we have the option of displaying or hiding a virtual machine table.
Select an item that you want to machine using Export Tuning or export to the WOP environment.
In the template window you will find further options for optimizing your workpiece.

---

# Export Tuning : Panel
Select whether the workpiece is to be made from an unformatted raw plate or an already formatted prefabricated plate.

---

# Export Tuning : Formatting Type
Select how to format.

---

# Export Tuning : Machinings Before Formatting
Check the box if formatting is to be done after machining.

---

# Export Tuning : Non-Rectangular Cuts After Formatting
Place a tick if the diagonal cuts or chamfering is to be made after the edge processing.

---

# Export Tuning : Stage Order
Select whether the workpiece should receive the edge before or after machining.

---

# Export Tuning : Sides Order
Specify whether the outer/inner side of the workpiece is to be machined first.

---

# Export Tuning : Merge Export Programs
Specify how the programs of the editing sides are to be exported.

---

# Export Tuning : Using Mirrors
Select whether the workpiece to be machined on both sides is to be machined on the mirrored workplace in the second side machining.

---

# Export Tuning : Use NC Stop
Select whether the workpiece to be machined on both sides is to be machined by NC stop in the second side machining in the same program.

---

# Export Tuning : Two Plates, Using Mirrors: Dont´t Merge
Select whether the workpiece to be machined on both sides is to be machined in the second side machining in a separate programs.

---

# Export Tuning : Auto PLace
Place a tick if the workpiece is to be positioned as in the option setting. Remove the tick if you want to change the positioning manually.

---

# Export Tuning : Use retractable stop bold
Set a check mark if you use fold-out fences for machining the workpiece.

---

# Export Tuning : Formatting Prod. Part Offset
Specify the desired production part offset dimension, of the workpiece when formatting on the machine.

---

# Export Tuning : Stage 1
SmartWOP shows you how and in which order the processing steps are carried out.

---

# Export Tuning : Tool Numbers
Specify a desired tool number for machining for the selected workpiece. If you do not make any changes, the tools from the option setting are used.

---

# Export Tuning : Profile
Change settings in your WOP environment by duplicating the design and making changes in the duplicate.
It is important that you create a duplicate, as the pattern is reset to default after each update to avoid potential errors.

---

# Export Tuning : Machine Set-UP Configuration
Select on which machine the workpiece is to be machined.

---

# Center View
Click Center View to centre the view on the selected item or volume

---

# Create new folder
In the Materials library, click Create new folder to make a new folder and name it. You can also open an existing folder before clicking to create a subfolder

---

# Create materials from texture folder
To quickly create many materials, first create a subfolder then choose Automatically create materials from texture folder. In the dialog select panel thicknesses and edge thicknesses, add new panel materials (specifying raw material, thickness and supplier) and add new edge materials (specify name, article number, supplier, thickness, width and minimum/maximum panel thickness). Repeat this for all thicknesses you use. Then click Generate panel names to have SmartWOP generate names with décor and thickness or just thickness. Select the folder containing texture images, ensure the grain runs along the X‑direction and change the angle to 90° if necessary. Start the import; SmartWOP creates materials for each specified plate and edge thickness

---

# Creating room materials
To create room design materials, create a folder (e.g. “Room design”) and click New to create a material. Give it a name (e.g. wall plaster) and choose the material type. In the Surface Texture and Section Texture columns select textures from your texture folder, optionally rotate or mirror them. For plain‑coloured materials you can allow grain rotation, but for wood decors or directional decors leave this unchecked. Under Display Settings you can set reflection levels and glossiness

---

# Create new Custom Material
To create your own material, optionally create a folder (e.g. “Own materials”) and click New. Give the material a name and specify whether it is coated board, raw material, metal, plastic or glass. Choose surface and cutting‑edge textures, adjust angles and mirrors as needed, and optionally allow grain rotation for non‑directional decors. Use Display Settings to set reflection, specular level and glossiness. You can add new panel or edge materials via the corresponding buttons

---

# Duplicate Material
Use the Duplicate button to make a copy of a material. Duplicates open automatically for editing so you can adjust them without changing the original

---

# Edit Material
Select a material and click Edit to modify it. You can change the material name and type (noting whether wood‑based materials are multi‑layer or single‑layer), choose new textures for surfaces and sections via the three dots, adjust angles and mirror settings, allow rotation for non‑directional materials, adjust display settings (reflection level, specular level, glossiness) and add panel or edge materials

---

# Material Picker
Click Material Picker to quickly find materials already applied in your created material folders

---