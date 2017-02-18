import json

# open the 
f = open('data/library.bib', 'r')
publications = []
for line in f:
    if 'author' in line[0:15]:
        line = line[10:-3]
        line = line.replace('\`', '')
        line = line.replace('\'', '')
        line = line.replace('\\', '')
        line = line.replace('{', '')
        line = line.replace('}', '')
        line = line.replace(',', '')
        line = line.replace('"', '')
        line = line.replace('-', '')
        line = line.replace('.', '')
        publications.append(line)
        
# create the nodes (authors)
authors_list = []
for authors in publications:
    authors_ = authors.split(' and ') # we assume that each authors are separated by ' and ' (standard from Mendeley)
    for author in authors_:
        author = author[0:(author.index(' ')+2)]
        if not author in authors_list:
            authors_list.append(author)

#remove the authors with a single publications
publication_quantity = []
clean_authors_list = []
for author in authors_list:
	author = author[0:(author.index(' ')+2)]
	i = 0
	for authors in publications:
		if author in authors:
			i = i +1
	if i >1:
		publication_quantity.append(i)
		print('%s has published %d papers' % (author, i))
		clean_authors_list.append(author)

print('Final authors list')
print(clean_authors_list)

authors_list = clean_authors_list

# add the edges (co-authors)
data = []
i = 0
for author in authors_list:
	dico = dict()
	links = []
	for authors_publication in publications:
		if author in authors_publication:
			authors_ = authors_publication.split(' and ')
			for name in authors_:
				name = name[0:(name.index(' ')+2)]
				if name in authors_list:
					links.append(name)
	dico['name'] = author
	dico['size'] = publication_quantity[i]*publication_quantity[i]*publication_quantity[i]*1000
	dico['imports'] = links
	data.append(dico)
	i = i+1

# write file in .json
with open('data/data.json', 'w') as outfile:
    json.dump(data, outfile)
