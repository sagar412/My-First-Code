#Printing_models example, chapter 8{Functions}
unprinetd_designs = ['phone case','robot pendent','shoes','umbrella']
completed_models = []

def print_models(unprinetd_designs,completed_models):
    while unprinetd_designs:    
          current_design = unprinetd_designs.pop()
          print(f"Now Printing: {current_design}")
          completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\n The printing of following models are done:")
    for models in completed_models:
        print(f"{models.title()}")


print_models(unprinetd_designs,completed_models)
show_completed_models(completed_models)
