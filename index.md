# The OSync Specification

## Why OSync?
Sure we have RSS, RDF, and Atom which I have been working with for many years. There is one big issues with these formats… They all use XML which tends to be wordy and more importantly XML is overly complex to parse especially in languages like Javascript, PHP, Ruby and Python. However JSON thankfully is!

While developing this format I set out with the following goals:

* Easy/fast to parse and implement
* Make it so feeds and items are location aware
* a proper tagging system for feeds/items/attachments
* multiple attachments
* Able to be used cross-site/domain
* Uses JSONP
* Incorporate some of the RSS extension elements that were used in common implementations

## Specification
### Main Elements
* id: Unique ID for the feed itself, great for using in conjunction with SUP, PubSubHubbub or rssCloud
* hub: A central place to see which OSync feeds have been updated. Usually a location for a servers SUP, PubSubHubbub or rssCloud location (Optional)
* title: Title of the feed
* subtitle: Subtitle for this feed (Optional)
* summary: A short description of this feed (Optional)
* permalinkUrl: permalinkUrl to where on this content came from
* lang: Based on the W3C standard language codes
* copyrite: A string describing the copyrite for this feed
* copyriteImage: Image representation of copyrite, such as a Creative Commons logo (Optional)
* location: See Location (Optional)
* postedTime: Date the feed was first published in ISO 8601 format example: 2009-08-05T11:17Z
* updatedDate: Last time the feed was updated (Optional)
* generator: What application/script created this output. Helpful for debugging. (Optional)
* categories: See Categoies (Optional)
* image: Should be a square .jpg image that is at least 600 x 600 pixels
* thumbnail: A thumbnail version (32x32) of the image in the ‘image’ key
* items: A list of items (see below for item description)

### Globals
**Location**

* name: The name for the location (Optional)
* address: Street Address (Optional)
* city: City, Town, or Village for the location (Optional)
* state: State or Provence (Optional)
* zip: ZIPCODE or Postal Code (Optional)
* latitude: Latitude (Optional if longitude not specified)
* longitude: Longitude (Optional if latitude not specified)

**Categories**

* categories: A list of categories/keywords/tags that you wish to associate with this item

### Items
* id: Unique ID for this item
* title: title for this item
* permalinkUrl: Permanent URL of where to find this item
* sources: A list of sources for this item. Sites like digg.com might want to specify the original article here. (Optional)
* location: See Location (Optional)
* postedTime: Date item was first published in ISO 8601 format example: 2009-08-05T11:17Z
* updatedDate: Last time the item was updated (Optional)
* summary: A short description of this item (Optional)
* body: The full text for this item
* author: Defines the author for this item (see below for description)
* contributors: a list of authors that also contributed to this item (see author description below) (Optional)
* categories: See Categoies (Optional)
* attachments: A list of attached resources for this item (see below for description) (Optional)

**Author**

* name: Full name of the author
* permalinkUrl: Permanent URL of where you can find the author online
* email: E-Mail address of where you can contact the author (Optional)

**Attachments**

* id: Unique ID for this attachment
* filename: Allows you to specify a specific name for this file (Optional)
* permalinkUrl: Permanent URL of where to find this attachment
* postedTime: Date item was first published in ISO 8601 format example: 2009-08-05T11:17Z
* mimeType: mime-type that defines what type of attachment this is
* bytes: Attachment size in bytes
* duration: Duration in seconds, should be specified if type is audio or video (Optional)
* location: See Location (Optional)
* categories: See Categoies
* hash: Hash for the file. Hashes are useful to help the consumer that they downloaded the file correctly. Prefix hashes with the hashing algorithm followed by a dash for example “md5-5b7c86d36cf17ada4853b1cbbdedf47f” (Optional)
* explicit: Does the content contain explicit material? False if not specified (Optional)
* hidden: This should stop a consumer from showing this file in their UI. False if not specified (Optional)

### Example
```
{
    "categories": [
        "web",
        "formats",
        "specifications"
    ],
    "copyrite": "Creative Commons Attribution-Noncommercial-No Derivative Works 3.0",
    "copyriteImage": "http://creativecommons.org/images/public/somerights20.png",
    "generator": "TextMate http://macromates.com/",
    "id": "c4dfcb75-8cd5-47e1-8a09-b19141ec2df8",
    "image": "http://www.osync.org/media/osync-600x600.jpg",
    "items": [
        {
            "attachments": [
                {
                    "bytes": 228223,
                    "duration": 923282,
                    "explicit": false,
                    "filename": "osync-podcast-01.mp3",
                    "hash": "md5-6c6d81147f00bd6adb710d22bfe69f05",
                    "hidden": false,
                    "id": "25746ef0-b362-4d38-b4e6-a0443c634d7e",
                    "permalinkUrl": "http://www.osync.org/pcasts/osync-podcast-01.mp3",
                    "postedTime": "2009-08-05T11:17Z",
                    "type": "audio/mpeg"
                }
            ],
            "author": {
                "email": "ray.slakinski@gmail.com",
                "name": "Ray Slakinski",
                "permalinkUrl": "http://www.slakinski.com"
            },
            "body": "We lauched OSync today! we had a big party and it was all kinds of fun. I hope you like it!",
            "categories": [
                "web",
                "formats",
                "specifications"
            ],
            "exeprt": "We lauched OSync today!",
            "id": "fd8e3a0e-5786-4583-9baa-bb65537eed70",
            "location": {
                "address": "2383 Dundas Street West",
                "city": "Oakville",
                "latitude": 43.439957,
                "longitude": -79.772071999999994,
                "name": "Funky Thai",
                "state": "Ontario",
                "zip": "L6M3X2"
            },
            "permalinkUrl": "http://www.osync.org/posts/osync-launched",
            "postedTime": "2009-08-05T11:17Z",
            "sources": [
                "http://www.osync.org"
            ],
            "title": "OSync Launched!",
            "updatedDate": "2009-08-05T11:17Z"
        }
    ],
    "lang": "en",
    "location": {
        "address": "2383 Dundas Street West",
        "city": "Oakville",
        "latitude": 43.439957,
        "longitude": -79.772071999999994,
        "name": "Funky Thai",
        "state": "Ontario",
        "zip": "L6M3X2"
    },
    "permalinkUrl": "http://www.osync.org",
    "postedTime": "2009-08-05T11:17Z",
    "subtitle": "Content Syndcation via JSONP",
    "summary": "All the news you can use about your favorite new web syndication format OSync",
    "thumbnail": "http://www.osync.org/media/osync-32x32.jpg",
    "title": "News about OSync",
    "updatedDate": "2009-08-05T12:17Z"
}
```
