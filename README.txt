Python Static Site Generator for a blog

1. Open the config file (config.json) and retrieve the output folder where the site will be generarted to
2. Delete the current instance of the output folder, to start afresh.
3. Copy the assets over from the /assets folder to the /{outputFolder}/assets folder
4. For each collection (posts and pages), cycle through the posts folder:
    - convert each file from markdown to HTML
    - render the template
    - save to the outputFolder
5. Generate the homepage from the list of posts
6. Show how many files have been created in how much time