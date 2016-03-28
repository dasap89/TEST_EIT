from django.shortcuts import render
from comp_struct.models import Company


def index(request):
  tree = Company.fix_tree()
  annotated_list = Company.get_annotated_list()
  root = Company.objects.all().first()

  my_element=[]
  result_list = []
  list_of_desc = []

  for i in range(len(annotated_list)):
    annotated_list[i][0].name = '-' * (annotated_list[i][1]['level'] + 1) + ' ' + annotated_list[i][0].name
    my_element = list(annotated_list[i])
    node = annotated_list[i][0]
    
    if node.is_leaf() is False:
        list_of_desc = list(node.get_descendants())
        sum_children = 0
    
        for i in list_of_desc:
            sum_children += i.earnings
        sum_children += node.earnings

    else:
        sum_children = None

    my_element.append(sum_children)
    result_list.append(my_element)

  return render(request, "index.html", {'annotated_list': result_list})
