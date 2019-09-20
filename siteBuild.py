from datetime import date, datetime, timedelta
import json, time, requests, os, sys, shutil
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
import sass

# Start the timer...
startTime = time.time()

# Open the config file and get the content and output folders
fname = './config.json'
with open(fname, 'r') as f:
    data = json.load(f)

siteConfig = data

# Get the output folder from the config file. If there isn't one, default to 'site'
if data['outputDestination']:
    outputFolder = data['outputDestination']
else:
    outputFolder = 'site'

# Get the collections object from the config file. If there isn't one, default to pages and posts
if data['collections']:
    collections = data['collections']
else:
    collections = ["pages", "posts"]

# Get the data object from the config file. If there isn't one, default to data folder
if data['dataFolder']:
    dataFolder = data['dataFolder']
else:
    dataFolder = 'data'

# For each file in data, grab it, add to a list, and add to site object
if os.path.isdir(f"{outputFolder}"):
    dataForSite = []
    dataFiles = [x for x in os.listdir(f"./{dataFolder}") if x.endswith(".json")]
    for d in dataFiles:
        dataFName = os.path.splitext(d)[0]
        dataFNameExt = os.path.splitext(d)[1]
        fname = f"./{dataFolder}/{d}"
        with open(fname, 'r') as f:
            dataFetched = json.load(f)
        dataForSiteIndiv = { dataFName: dataFetched }
        dataForSite.append(dataForSiteIndiv)
        # print(dataForSite)
    siteConfig['data'] = dataForSite
    # print(siteConfig)
        
# Remove the existing output folder
if os.path.isdir(f"{outputFolder}"):
    shutil.rmtree(f"{outputFolder}")

# if there is an assets object in config, copy the Assets over
if data['assets']:
    assetSource = data['assets']['assetSource']
    assetDestination = data['assets']['assetDestination']
    assetSourcePath = f"./{assetSource}"
    assetDestinationPath = f"./{outputFolder}/{assetDestination}"

    if os.path.isdir(assetSource):
        # os.makedirs(assetDestinationPath, exist_ok=True)  # Force the creation of the target folder
        shutil.copytree(assetSourcePath, assetDestinationPath)
        print(f"Assets copied to the {assetDestinationPath} folder")
    else:
        print(f"Assets source folder does not exist: {assetSource}")

# If there is Sass object in the config, process the Sass
if data['sass']:
    sassFolder = data['sass']['sassFolder']
    sassOutput = data['sass']['sassOutput']
    if os.path.isdir(sassFolder):
        sass.compile(dirname=('sass', f"{outputFolder}/assets/css"))
        print('Sass file compiled and created')
    else:
        print(f"Sass source folder does not exist: {sassFolder}")

# Build the list of pages and posts
collectionPageList = []
for c in collections:
    # Check if the collection folder exists...
    if os.path.isdir(c):
        for cp in os.listdir(c):
            collectionPagePath = os.path.join(c, cp)
            with open(collectionPagePath, 'r') as f:
                parsedCollectionPage = markdown(f.read(), extras=['metadata'])

            collectionPageMetaData = parsedCollectionPage.metadata
            collectionPageHTML = parsedCollectionPage

                # Start with the collectiion data as the collection page meta data
            collectionPageData = {}
            collectionPageData['metadata'] = collectionPageMetaData


            # Next determine the permalink and templates
            if collectionPageMetaData['type'] == 'post':
                # Set the template to the post template
                template = "post.html"
                # Construct the permalink from the title and date
                postFileName = os.path.splitext(cp)[0]
                permalink = f"{postFileName[:10].replace('-','/')}/{postFileName[11:]}"
            elif collectionPageMetaData['type'] == 'page':
                # Set the template to the page template
                template = "page.html"
                # Construct the permalink from filename without extension
                permalink = os.path.splitext(cp)[0]
            elif collectionPageMetaData['type'] == 'blog':
                # Set the template to the page template
                template = "blog.html"
                # Construct the permalink from filename without extension
                permalink = os.path.splitext(cp)[0]
            elif collectionPageMetaData['type'] == 'home':
                # Set the template to the page template
                template = "homepage.html"
                # Construct the permalink from filename without extension
                permalink = ""
                
            collectionPageData['permalink'] = permalink

            # Now pickup the metadata from the actual collection page and set the object

            # Finally add the content of the parsed HTML
            collectionPageData['content'] = collectionPageHTML                
            # Add to the collection page list dict
            collectionPageList.append(collectionPageData)
    else:
        print(f"Collection folder does not exist - {c}")

# Make a page list and post list
pageList = []
postList = []
if len(collectionPageList) > 0:
    pageList = [p for p in collectionPageList if p['metadata']['type'] in ['page','blog','home']]
    postList = [p for p in collectionPageList if p['metadata']['type'] == 'post']

    # Sort the list of posts in reverse order by date
    if len(postList) > 0:
        postList.sort(key=lambda p: datetime.strptime(p['metadata']['date'], '%Y-%m-%d'), reverse=True)

# Generate all the posts and pages in collectionPageList
# Rendering with Jinja
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
# Now loop through items
for cpl in collectionPageList:
    if cpl['metadata']['type'] == 'post':
        template = 'post.html'
    elif cpl['metadata']['type'] == 'page':
        template = 'page.html'
    elif cpl['metadata']['type'] == 'blog':
        template = 'blog.html'
    elif cpl['metadata']['type'] == 'home':
        template = 'homepage.html'
    elif cpl['metadata']['type'] == 'contact':
        template = 'contact.html'

    permalink = cpl['permalink']
    
    # Create target file, path and html, and write to file
    test_template = env.get_template(template)
    if cpl['metadata']['type'] in ['blog','home']:
        targetHTML = test_template.render(post=postList, site=siteConfig)
    else:
        targetHTML = test_template.render(post=cpl, site=siteConfig)

    targetpath = f"./{outputFolder}/{permalink}"
    targetfile = f"{targetpath}/index.html"
    os.makedirs(targetpath, exist_ok=True)  # Force the creation of the target folder
    with open(targetfile, 'w') as file:
        file.write(targetHTML)


# Generate the homepage from postList
# Make a page list and post list
# pageList = []
# postList = []
# if len(collectionPageList) > 0:
#     pageList = [p for p in collectionPageList if p['metadata']['type'] == 'page']
#     postList = [p for p in collectionPageList if p['metadata']['type'] == 'post']

#     # Sort the list of posts in reverse order by date
#     if len(postList) > 0:
#         postList.sort(key=lambda p: datetime.strptime(p['metadata']['date'], '%Y-%m-%d'), reverse=True)

# Rendering the homepage with Jinja
# test_template = env.get_template('homepage.html')
# targetHTML = test_template.render(post=postList, site=siteConfig)
# targetpath = f"./{outputFolder}"
# targetfile = f"{targetpath}/index.html"
# os.makedirs(targetpath, exist_ok=True)  # Force the creation of the target folder
# with open(targetfile, 'w') as file:
#     file.write(targetHTML)

# print("Homepage generated")


# ... and stop the timer!
endTime = time.time()
duration = endTime - startTime
print(f"Generator took {str(round(duration, 3))} seconds to generate:")
if len(pageList) == 1:
    print(f" - {len(pageList)} page")
else:
    print(f" - {len(pageList)} pages")

if len(postList) == 1:
    print(f" - {len(postList)} post")
else:
    print(f" - {len(postList)} posts")
