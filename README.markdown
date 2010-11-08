# The oSync Specification #

## Why oSync? ##

Sure we have [RSS](http://cyber.law.harvard.edu/rss/rss.html), [RDF](http://www.w3.org/TR/REC-rdf-syntax/), 
and [Atom](http://www.atomenabled.org/developers/syndication/atom-format-spec.php) which I have been working with 
for many years. There are two big issues with these formats... They all use 
[XML](http://en.wikipedia.org/wiki/XML) which tends to be wordy and more importantly XML is not overly easy to parse 
especially in langs like Javascript, PHP, Ruby and Python. However [JSON](http://en.wikipedia.org/wiki/JSON) thankfully is! 

While developing this format I set out with the following goals:

* Easy/fast to parse and implement
* Make it so feeds and items are location aware
* a proper tagging system for feeds/items/attachments
* multiple attachments
* Able to be used cross-site/domain
  * Uses [JSONP](http://en.wikipedia.org/wiki/JSON#JSONP)
* Incorporate some of the RSS extension elements that were used in common implementations

### Note ###

This specification is considered ALPHA, and not ready for production use as it could change, I welcome everyone to please
come and comment in the [oSync Development Google Group](http://groups.google.com/group/osync-development)

### Example ###

    {
        "updatedDate": "2009-08-05T12:17Z",
        "subtitle": "Content Syndcation via JSONP",
        "id": "c4dfcb75-8cd5-47e1-8a09-b19141ec2df8",
        "lang": "en",
        "title": "News about oSync",
        "image": "http://www.osync.org/media/osync-600x600.jpg",
        "generator": "TextMate http://macromates.com/",
        "permalinkUrl": "http://www.osync.org",
        "summary": "All the news you can use about your favorite new web syndication format oSync",
        "copywrite": "Creative Commons Attribution-Noncommercial-No Derivative Works 3.0",
        "copywriteImage": "http://creativecommons.org/images/public/somerights20.png",
        "postedTime": "2009-08-05T11:17Z",
        "imageThumbnail": "http://www.osync.org/media/osync-32x32.jpg",
        "categories": [
            "web",
            "formats",
            "specifications" 
        ],
        "location": {
            "name": "Funky Thai",
            "address": "2383 Dundas Street West",
            "city": "Oakville",
            "state": "Ontario",
            "zip": "L6M3X2",
            "geolat": 43.439957,
            "geolong": -79.772072 
        },
        "items": [
            {
                "updatedDate": "2009-08-05T11:17Z",
                "body": "We lauched oSync today! we had a big party and it was all kinds of fun. I hope you like it!",
                "id": "fd8e3a0e-5786-4583-9baa-bb65537eed70",
                "title": "oSync Launched!",
                "author": {
                    "email": "ray.slakinski@gmail.com",
                    "name": "Ray Slakinski",
                    "permalinkUrl": "http://www.slakinski.com"
                },
                "sources": [
                    "http://www.osync.org"
                ],
                "permalinkUrl": "http://www.osync.org/posts/osync-launched",
                "location": {
                    "name": "Funky Thai",
                    "address": "2383 Dundas Street West",
                    "city": "Oakville",
                    "state": "Ontario",
                    "zip": "L6M3X2",
                    "geolat": 43.439957,
                    "geolong": -79.772072 
                },
                "exeprt": "We lauched oSync today!",
                "postedTime": "2009-08-05T11:17Z",
                "categories": [
                    "web",
                    "formats",
                    "specifications" 
                ],
                "attachments": [
                    {
                        "hash": "6c6d81147f00bd6adb710d22bfe69f05",
                        "id": "25746ef0-b362-4d38-b4e6-a0443c634d7e",
                        "postedTime": "2009-08-05T11:17Z",
                        "explicit": false,
                        "permalinkUrl": "http://www.osync.org/pcasts/osync-podcast-01.mp3",
                        "hashType": "md5",
                        "filename": "osync-podcast-01.mp3",
                        "duration": 923282,
                        "type": "audio/mpeg",
                        "blockConsumer": false,
                        "bytes": 228223
                    }
                ]
            }
        ]
    }

## Specification ##

### Main Elements ###

* id: Unique ID for the feed itself, great for using in conjunction with [SUP](http://code.google.com/p/simpleupdateprotocol/), [PubSubHubbub](http://code.google.com/p/pubsubhubbub/) or [rssCloud](http://rsscloud.org/)
* hub: A central place to see which oSync feeds have been updated. Usually a location for a servers [SUP](http://code.google.com/p/simpleupdateprotocol/), [PubSubHubbub](http://code.google.com/p/pubsubhubbub/) or [rssCloud](http://rsscloud.org/) location _(Optional)_
* title: Title of the feed
* subtitle: Subtitle for this feed _(Optional)_
* summary: A short description of this feed _(Optional)_
* permalinkUrl: permalinkUrl to where on this content came from
* lang: Based on the [W3C standard language codes](http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes)
* copywrite: A string describing the copywrite for this feed
* copywriteImage: Image representation of copywrite, such as a [Creative Commons](http://creativecommons.org/) logo _(Optional)_
* location: See [Location](#) _(Optional)_
* postedTime: Date the feed was first published in [ISO 8601](http://en.wikipedia.org/wiki/ISO-8601) format example: 2009-08-05T11:17Z
* updatedDate: Last time the feed was updated _(Optional)_
* generator: What application/script created this output. Helpful for debugging. _(Optional)_
* categories: See [Categoies](#) _(Optional)_
* image: Should be a square .jpg image that is at least 600 x 600 pixels
* imageThumbnail: A thumbnail version (32x32) of the image in the 'image' key
* items: A list of items (see below for item description)

### Globals ###

#### Location ####

* name: The name for the location _(Optional)_
* address: Street Address _(Optional)_
* city: City, Town, or Village for the location _(Optional)_
* state: State or Provence _(Optional)_
* zip: ZIPCODE or Postal Code _(Optional)_
* geolat: Latitude _(Optional if geolong not specified)_
* geolong: Longitude _(Optional if geolat not specified)_

#### Categories ####

* categories: A list of categories/keywords/tags that you wish to associate with this item

### Items ###

* id: Unique ID for this item
* title: title for this item
* permalinkUrl: Permanent URL of where to find this item
* sources: A list of sources for this item. Sites like digg.com might want to specify the original article here. _(Optional)_
* location: See [Location](#) _(Optional)_
* postedTime: Date item was first published in [ISO 8601](http://en.wikipedia.org/wiki/ISO-8601) format example: 2009-08-05T11:17Z
* updatedDate: Last time the item was updated _(Optional)_
* summary: A short description of this item _(Optional)_
* body: The full text for this item
* author: Defines the author for this item (see below for description)
* contributors: a list of authors that also contributed to this item (see author description below) _(Optional)_
* categories: See [Categoies](#) _(Optional)_
* attachments: A list of attached resources for this item (see below for description) _(Optional)_

#### Author ####

* name: Full name of the author
* permalinkUrl: Permanent URL of where you can find the author online
* email: E-Mail address of where you can contact the author _(Optional)_

#### Attachments ####

* id: Unique ID for this attachment
* filename: Allows you to specify a specific name for this file _(Optional)_
* permalinkUrl: Permanent URL of where to find this attachment
* postedTime: Date item was first published in [ISO 8601](http://en.wikipedia.org/wiki/ISO-8601) format example: 2009-08-05T11:17Z
* mimeType: [mime-type](http://www.webmaster-toolkit.com/mime-types.shtml) that defines what type of attachment this is
* bytes: Attachment size in bytes
* duration: Duration in seconds, should be specified if type is audio or video _(Optional)_
* location: See [Location](#) _(Optional)_
* categories: See [Categoies](#)
* hash: [Hash for the file](http://www.electrictoolbox.com/article/linux-unix-bsd/howto-check-md5-file/). Hashes are useful to help the consumer that they downloaded the file correctly _(Optional)_
* hashType: To be specified if hash is set and is not MD5 (MD5 is assumed) _(Optional)_
 * Note: Use lowercase (md5, sha256)
* explicit: Does the content contain explicit material? False if not specified _(Optional)_
* blockConsumer: This should stop a consumer from showing this file in their UI. False if not specified _(Optional)_

<a rel="license" href="http://creativecommons.org/licenses/by-nd/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://creativecommons.org/images/public/somerights20.png" /></a>