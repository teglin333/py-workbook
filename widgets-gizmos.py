# read the number of widgets and gizmos and display the total weight of the parts

weight_gizmo = 112
weight_widget = 75

quantity_gizmos = int(input('Enter the number of gizmos: '))
quantity_widgets = int(input('Enter the number of widgets: '))

total_weight = (weight_gizmo * quantity_gizmos) + (weight_widget * quantity_widgets)

print('The total weight of the parts is: %d grams.' % total_weight)