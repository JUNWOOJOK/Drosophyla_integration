import sys
import collections
names_dmp=sys.argv[1]
kraken_output=sys.argv[2]
dict_a=collections.defaultdict()
list_b=[]
with open(names_dmp) as file:
    for line in file:
        taxid=line.split("|")[0].strip()
        sciname=line.split("|")[1].strip()
        dict_a[taxid]=sciname


#for i,l in dict_a.items():
#    print(i,l,sep="\t")
dict_a["0"]="Unclassified"
def integration_judge(input_line):
    bbb=collections.defaultdict(int)
    for i in input_line.split():
        scinames=dict_a[str(i.split(":")[0])]
        bbb[scinames]+=int(i.split(":")[1])
    return(bbb)


with open(kraken_output) as file:
    for line in file:
        linename=line.split("\t")[1]
        return_dict=integration_judge(line.split("\t")[4])
        list_a=list(return_dict.keys())
        if ('fruit fly' in  list_a) and (len(set(list_a)-set(['Unclassified','cellular organisms']))>2):
#            print(list(return_dict.keys()))
            for i,l in return_dict.items():
                list_b.append(i)

print(collections.Counter(list_b))
        
