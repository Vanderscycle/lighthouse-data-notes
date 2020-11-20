# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class GroceryitemindexerPipeline:

    def __init__(self):
        # requires two arguments
        self.conn = pymongo.MongoClient(
            '127.0.0.1',27017)
        

        dbnames = self.conn.list_database_names()
        if 'groceryStore' not in dbnames:
            # creating the database
            # mongodb doesn't take capitilization
            self.db = self.conn['groceryStore']

        #the database already exists
        else:
            # we acces the db

            self.db = self.conn.groceryStore

        dbCollectionNames = self.db.list_collection_names()
        if 'amazonWholeFood' not in dbCollectionNames:
            self.collection = self.db['amazonWholeFood']
        
        else:
            # we acces the db
            self.collection = self.db.amazonWholeFood

    def process_item(self, item, spider):

        # We can have issues on
        try:
            # insert Many requires a dict of dict. i
            self.collection.insert_one(dict(item))
            # self.collection.update(dict(item),{ 'upsert': 'true' })
        
        except Exception as e:
            print('\n','--- ERROR ---',e,'\n')
        # in the future 
        
        # it makes more sense to do it after in the shell. Let scrapy handle the collection and mongodb the cleaning
        #self.collection.update(dict(item)) #
        #self.db.AmazonWholeFood.createIndex({'name':1},{'spider':2},{'unique':true,'dropDups':true});

        for k,v in item.items():
            print(f'key/value: {k} : {v}')
        return item

# what we can is a weekly transferfrom activity db to a historic db 
# to set historic storage  (mongo db)
# cool mongo db quick command
# # amazon being a collection
# db.amazonWholeFood.count()
# # drop the collection
# db.amazonWholeFood.drop()
