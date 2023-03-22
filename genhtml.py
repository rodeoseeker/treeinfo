#!/usr/bin/python3

import os
import json
import random

def genHtml():
    dirname='./tree_data'
    fname="./tree_info.html"
    if not os.path.exists(dirname):
        return;

    subfolders = [ f.name for f in os.scandir(dirname) if f.is_dir() ]
    subfolders.sort(key = lambda a : int(a))
    intfolders = [int(x) for x in subfolders]
    random.shuffle(intfolders)
    intset=[x for x in range(0,5)]
    random.shuffle(intset)
    offset = intset[0]

    with open(fname, "w") as ofile:
        print('<!DOCTYPE html>', file=ofile)
        print('<html>', file=ofile)
        print('  <head>', file=ofile)
        print('    <title>Image Gallery</title>', file=ofile)
        print('  </head>', file=ofile)
        print('  <body>', file=ofile)
        folder = str(intfolders[0])
        if not os.path.exists(os.path.join(dirname, folder, 'links.json')):
            print(f'links json not found for {folder}')
            return
        with open(os.path.join(dirname, folder, 'links.json')) as json_file:
            keys = ["leaves", "flowers", "fruit", "twig", "bark", "whole tree"]
            links = json.load(json_file)
            ii = offset
            print(f'  <div id="image-set{ii+1}" style="display: block;">', file=ofile)
            for jj, key in enumerate(keys):
                '''
                print(f'      <a href="{links[key][ii]}"><img src="{links[key][ii]}" height="250" id="image{jj+1}" style="display: inline-block;"></a>', file=ofile)
                '''
                print(f'      <img src="{links[key][ii]}" height="250" id="image{jj+1}" style="display: inline-block;">', file=ofile)
            print(f'  </div>', file=ofile)

        print('<div id="caption-container" style="display: none">', file=ofile)
        for folder in subfolders:
            with open(os.path.join(dirname, folder, 'namekey.txt')) as namekey_file:
                namekey = namekey_file.read()
                print(f'  <p id="caption{folder}" style="display: none;">{namekey}</p>', file=ofile)
                print(folder, namekey)
        print('</div>', file=ofile)
        print('    <button onclick="showPreviousImage()">Previous</button>', file=ofile)
        print('    <button onclick="showNextImage()">Next</button>', file=ofile)
        print('    <button onclick="toggleCaption()">Reveal</button>', file=ofile)
        print('    <script>', file=ofile)
        print('const image_links = ', file=ofile)
        image_links=[]
        for folder in subfolders:
            with open(os.path.join(dirname, folder, 'links.json')) as json_file:
                keys = ["leaves", "flowers", "fruit", "twig", "bark", "whole tree"]
                links = json.load(json_file)
                image_set_links=[]
                for ii in range(5):
                    image_set=[]
                    for key in keys:
                        image_set.append(links[key][ii])
                    image_set_links.append(image_set)
                image_links.append(image_set_links)
        print('[', end='', file=ofile)
        for ii, imagegroupentry in enumerate(image_links):
            print('[', end='', file=ofile)
            for jj, image_set_entry in enumerate(imagegroupentry):
                if jj == len(imagegroupentry) - 1:
                    print(f'{image_set_entry}', file=ofile)
                else:
                    print(f'{image_set_entry},', file=ofile)
            if (ii == len(image_links)-1):
                print(']', file=ofile)
            else:
                print('],', file=ofile)
        print('];', file=ofile)
        numtrees=len(subfolders)
        print(f'const numImages = {numtrees};', file=ofile)
        indexes=[x-1 for x in intfolders]
        print(f'const shuffleGroup = {indexes};', file=ofile)
        print(f'const imageSetSize = {len(intset)}', file=ofile)
        print(f'const shuffleSet = {intset};', file=ofile)
        suffix='''
let currentImageIndex = 0;
      let currentImageSetIndex = 0;
      let imageOffset = shuffleGroup[currentImageIndex];
      let imageSetOffset = shuffleSet[currentImageSetIndex];

      function showNextImage() {
        hideCaption();
        currentImageIndex = (currentImageIndex + 1) % numImages;
        if(currentImageIndex == 0)
        {
          currentImageSetIndex = (currentImageSetIndex + 1) % imageSetSize;
        }
        imageOffset=shuffleGroup[currentImageIndex];
        imageSetOffset=shuffleSet[currentImageSetIndex];
        for(let ii = 1; ii <= 6; ii++)
        {
          const nextImage = document.getElementById(`image${ii}`);
          nextImage.src = image_links[imageOffset][imageSetOffset][ii - 1];
        }
        hideCaption();
      }

      function showPreviousImage() {
        hideCaption();
        if(currentImageIndex == 0)
        {
          currentImageSetIndex = (currentImageSetIndex - 1 + imageSetSize) % imageSetSize;
        }
        currentImageIndex = (currentImageIndex - 1 + numImages) % numImages;
        imageOffset=shuffleGroup[currentImageIndex];
        imageSetOffset=shuffleSet[currentImageSetIndex];
        for(let ii = 1; ii <= 6; ii++)
        {
          const prevImage = document.getElementById(`image${ii}`);
          prevImage.src = image_links[imageOffset][imageSetOffset][ii - 1];
        }
        hideCaption();
      }

      function toggleCaption() {
        const captionContainer = document.getElementById("caption-container");
        const caption = document.getElementById(`caption${imageOffset+1}`);
        if (captionContainer.style.display === "none") {
          caption.style.display = "block";
          captionContainer.style.display = "block";

        } else {
          hideCaption();
        }
      }

      function hideCaption() {
        const captionContainer = document.getElementById("caption-container");
        const caption = document.getElementById(`caption${imageOffset+1}`);
        caption.style.display = "none";
        captionContainer.style.display = "none";
        //caption.innerText = "";
      }
    </script>
  </body>
</html>

'''
        print(suffix, file=ofile)
        print(indexes)
        print(f'start offset: {offset}')



if __name__ == "__main__":
    genHtml()




