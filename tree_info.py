#!/usr/bin/python3
from  google_image_search import search_images
from fetch_image import fetch_image
import os
import json

def tree_links(tree_name):
    subqueries = ["leaves", "flowers", "fruit", "twig", "bark", "whole tree"]
    tree_image_links = {x:[] for x in subqueries}
    for subquery in subqueries:
        query=tree_name + " " + subquery
        #print(query)
        (links, retcode) = search_images(query)
        if (retcode != 200):
            return (tree_image_links, retcode)
        tree_image_links[subquery].extend(links)
    return (tree_image_links, retcode)

def save_content(dirname, filename, content, opentype):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    with open(os.path.join(dirname, filename), opentype) as f:
        f.write(content)

if __name__ == "__main__":
    subqueries = ["leaves", "flowers", "fruit", "twig", "bark", "whole tree"]
    treelist= [
        "Taxus brevifolia (Pacific Yew)",
        "Abies balsamea (Balsam Fir)",
        "Abies concolor (White Fir)",
        "Abies grandis (Grand Fir)",
        "Abies lasiocarpa (Subalpine Fir)",
        "Larix laricina (Tamarack)",
        "Larix occidentalis (Western Larch)",
        "Picea engelmannii (Engelmann Spruce)",
        "Picea glauca (White Spruce)",
        "Picea mariana (Black Spruce)",
        "Picea pungens (Blue Spruce)",

        "Taxodium distichum (Baldcyprus)",
        "Thuja occidentalis (Northern White-cedar)",
        "Thuja plicata (Western Redcedar)",
        "Sabal palmetto (Cabbage Palmetto)",
        "Washingtonia filifera (California Fan Palm)",
        "Populus angustifolia (Narrowleaf Cottonwood)",
        "Populus balsamifera (Balsam Poplar)",
        "Populus deltoides (Eastern Cottonwood)",
        "Populus fremontii (Fremont Cottonwood)",
        "Populus grandidentata (Bigtooth/Largetooth Aspen)",
        "Populus tremuloides (Quaking Aspen)",
        "Populus trichocarpa (Black Cottonwood)",
        "Salix bebbiana (Bebb Willow)",
        "Salix nigra (Black Willow)",
        "Salix scouleriana (Scouler Willow)",
        "Carya cordiformis (Bitternut Hickory)",
        "Carya glabra (Pignut Hickory)",
        "Carya illinoinensis (Pecan)",
        "Carya ovata (Shagbark Hickory)",
        "Juglans cinerea (Butternut)",
        "Juglans nigra (Black Walnut)",
        "Alnus rubra (Red Alder)",
        "Betula alleghaniensis (Yellow Birch)",
        "Betula lenta (Sweet Birch)",
        "Betula occidentalis (Water Birch)",
        "Betula papyrifera (Paper Birch)",
        "Betula populifolia (Gray Birch)",
        "Carpinus caroliniana (American Hornbeam)",
        "Ostrya virginiana (American/Eastern Hophornbeam)",
        "Castanea dentata (American Chestnut)",
        "Fagus grandifolia (American Beech)",
        "Lithocarpus densiflorus (Tanoak)",
        "Quercus agrifolia (Coast Live Oak)",
        "Quercus alba (White Oak)",
        "Quercus bicolor (Swamp White Oak)",
        "Quercus chrysolepis (CanyonLive Oak)",
        "Quercus douglasii (Blue Oak)",
        "Quercus falcata (Southern Red Oak)",
        "Quercus garryana (Oregon White Oak)",
        "Quercus imbricaria (Shingle Oak)",
        "Quercus kelloggii (California Black Oak)",
        "Quercus macrocarpa (Bur Oak)",
        "Quercus muehlenbergii (Chinkapin Oak)",
        "Quercus palustris (Pin Oak)",
        "Quercus prinus (Chestnut Oak)",
        "Quercus rubra (Northern Red Oak)",
        "Quercus velutina (Black Oak)",
        "Quercus virginiana (Live Oak)",
        "Celtis occidentalis (Northern Hackberry)",
        "Ulmus americana (American Elm)",
        "Ulmus rubra (Slippery Elm)",
        "Maclura pomifera (Osage-orange)",
        "Morus alba (White Mulberry)",
        "Morus rubra (Red Mulberry)",
        "Liriodendron tulipifera (Yellow-poplar)",
        "Magnolia grandiflora (Southern Magnolia)",
        "Magnolia macrophylla (Bigleaf Magnolia)",
        "Asimina triloba (Pawpaw)",
        "Sassafras albidum (Sassafras)",
        "Umbellularia californica (California-laurel)",
        "Hamamelis virginiana (Witch-hazel)",
        "Liquidambar styraciflua (Sweetgum)",
        "Platanus occidentalis (Sycamore)",
        "Platanus racemosa (California Sycamore)",
        "Amelanchier alnifolia (Western Serviceberry)",
        "Cercocarpus ledifolius (Curl-leaf Mountain Mahogany)",
        "Crataegus douglasii (Black Hawthorn)",
        "Crataegus pruinosa (Frosted Hawthorn)",
        "Heteromeles arbutifolia (Toyon)",
        "Prunus americana (American Plum)",
        "Prunus emarginata (Bitter Cherry)",
        "Prunus pensylvanica (Pin Cherry)",
        "Prunus serotina (Black Cherry)",
        "Prunus virginiana (Common Chokecherry)",
        "Sorbus americana (American Mountain-ash)",
        "Acacia farnesiana (Huisache/Sweet Acacia)",
        "Cercis canadensis (Eastern Redbud)",
        "Cercidium floridum (Blue Paloverde) synonym Parkinsonia florida",
        "Gleditsia triacanthos (Honeylocust)",
        "Gymnocladus dioicus (Kentucky Coffeetree)",
        "Prosopis glandulosa (Honey Mesquite)",
        "Robinia pseudoacacia (Black Locust)",
        "Zanthoxylum clava-herculis (Hercules-club/Toothache-Tree)",
        "Ailanthus altissima (Ailanthus/Tree of Heaven)",
        "Rhus glubra (Smooth Sumac)",
        "Ilex opaca (American Holly)",
        "Ilex vomitoria (Yaupon)",
        "Acer negundo (Boxelder)",
        "Acer rubrum (Red Maple)",
        "Acer saccharinum (Silver Maple)",
        "Acer saccharum (Sugar Maple)",
        "Aesculus californica (California Buckeye)",
        "Aesculus glabra (Ohio Buckeye)",
        "Tilia americana (American Basswood)",
        "Cereus giganteus (Saguaro)",
        "Eucalyptus globulus (Bluegum Eucalyptus)",
        "Cornus florida (Flowering Dogwood)",
        "Cornus nuttallii (Pacific Dogwood)",
        "Nyssa sylvatica (Black Tupelo/Blackgum)",
        "Arbutus menziesii (Pacific Madrone)",
        "Diospyros virginiana (Common Persimmon)",
        "Fraxinus americana (White Ash)",
        "Fraxinus latifolia (Oregon Ash)",
        "Fraxinus velutina (Arizona Ash)",
        "Catalpa bignonioides (Southern Catalpa)",
        "Catalpa speciosa (Northern Catalpa)",
        "Chilopsis linearis (Desert-willow)",
        "Sambucus canadensis (American Elder/Elderberry)",
        "Aleurites moluccana (Candlenut/Kukui)",
        "Picea rubens (Red Spruce)",
        "Picea sitchensis (Sitka Spruce)",
        "Pinus albicaulis (Whitebark Pine)",
        "Pinus aristata (Bristlecone Pine)",
        "Pinus attenuata (Knobcone Pine)",
        "Pinus banksiana (Jack Pine)",
        "Pinus contorta (Lodgepole Pine)",
        "Pinus echinata (Shortleaf Pine)",
        "Pinus edulis (Colorado Pinyon Pine)",
        "Pinus flexilis (Limber Pine)",
        "Pinus lambertiana (Sugar Pine)",
        "Pinus monophylla (Singleleaf Pinyon)",
        "Pinus monticola (Western White Pine)",
        "Pinus palustris (Longleaf Pine)",
        "Pinus ponderosa (Ponderosa Pine)",
        "Pinus resinosa (Red Pine)",
        "Pinus rigida (Pitch Pine)",
        "Pinus strobus (Eastern White Pine)",
        "Pinus taeda (Loblolly Pine)",
        "Pinus virginiana (Virginia Pine)",
        "Pseudotsuga menziesii (Douglas-fir)",
        "Tsuga canadensis (Eastern Hemlock)",
        "Tsuga heterophylla (Western Hemlock)",
        "Tsuga mertensiana (Mountain Hemlock)",
        "Chamaecyparis lawsoniana Port-Orford-cedar (Oregon Cedar)",
        "Cupressus macrocarpa (Monterey Cypress)",
        "Juniperus osteosperma (Utah Juniper)",
        "Juniperus scopulorum (Rocky Mountain Juniper)",
        "Juniperus virginiana (Eastern Redcedar)",
        "Sequoia sempervirens (Redwood)",
        "Sequoiadendron giganteum (Giant Sequoia)",
        "Ginkgo biloba (Ginkgo)"
    ]

    count=0
    for idx, treename in enumerate(treelist):
        if (os.path.exists(f'./tree_data/{idx+1}/links.json')):
            print(f'{idx + 1} : {treename } : Tree data already exists')
            continue
        count = count + 1
        print(f'{idx+1} : {treename}');
        (linkdict, retcode) = tree_links(treename);
        if (retcode != 200):
            print("query failed; quitting");
            quit()
        linkjson = json.dumps(linkdict)
        save_content(f'./tree_data/{idx+1}', f'namekey.txt', treename, 'w')
        save_content(f'./tree_data/{idx+1}', f'links.json', linkjson, 'w')
        if (count*6 > 95) :
            quit()


        '''
        for q in subqueries:
            for (num, link) in enumerate(linkdict[q]):
               (ext, content) = fetch_image(link)
               save_content(f'./tree_data/{idx+1}/{q}',f'img.{num+1}{ext}',content, 'wb')
        '''



#    print(tree_links("red alder"));
#    print(tree_links("black walnut"));


