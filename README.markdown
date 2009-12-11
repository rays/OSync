# The oSync Specification #

## Why oSync? ##

Sure we have [RSS](http://cyber.law.harvard.edu/rss/rss.html), [RDF](http://www.w3.org/TR/REC-rdf-syntax/), 
and [Atom](http://www.atomenabled.org/developers/syndication/atom-format-spec.php) which I have been working with 
for many years. There are two big issues with these formats... They all use 
[XML](http://en.wikipedia.org/wiki/XML) which tends to be wordy and more importantly XML is not overly easy to parse 
especially in languages like Javascript, PHP, Ruby and Python. However [JSON](http://en.wikipedia.org/wiki/JSON) thankfully is! 

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

### Sites uing oSync ###

None yet :( Be the first!

### Mailing List ###

<table border=0 style="background-color: #fff; padding: 5px;" cellspacing=0>
  <tr><td>
  <img src="http://groups.google.com/intl/en/images/logos/groups_logo_sm.gif"
         height=30 width=140 alt="Google Groups">
  </td></tr>
  <tr><td style="padding-left: 5px">
  <b>Subscribe to oSync Development</b>
  </td></tr>
  <form action="http://groups.google.com/group/osync-development/boxsubscribe">
  <tr><td style="padding-left: 5px;">
  Email: <input type=text name=email>
  <input type=submit name="sub" value="Subscribe">
  </td></tr>
</form>
<tr><td align=right>
  <a href="http://groups.google.com/group/osync-development">Visit this group</a>
</td></tr>
</table>

### Example ###

    {
         "updated_date": "2009-08-05T12:17Z",
         "subtitle": "Content Syndcation via JSONP",
         "uuid": "c4dfcb75-8cd5-47e1-8a09-b19141ec2df8",
         "language": "en",
         "title": "News about OSync",
         "image": "http://www.osync.org/media/osync-600x600.jpg",
         "generator": "TextMate http://macromates.com/",
         "uri": "http://www.osync.org",
         "summary": "All the news you can use about your favorite new web syndication format OSync",
         "copywrite": "Creative Commons Attribution-Noncommercial-No Derivative Works 3.0",
         "copywrite_image": "http://creativecommons.org/images/public/somerights20.png",
         "pub_date": "2009-08-05T11:17Z",
         "image_thumbnail": "http://www.osync.org/media/osync-32x32.jpg",
         "tags": 
         [
             "web",
             "formats",
             "specifications"
         ],
         "location": "43.437933,-79.754251",
         "items": 
        [
               {
                 "updated_date": "2009-08-05T11:17Z",
                 "body": "We lauched OSync today! we had a big party and it was all kinds of fun. I hope you like it!",
                 "uuid": "fd8e3a0e-5786-4583-9baa-bb65537eed70",
                 "title": "OSync Launched!",
                 "author": 
                {
                     "email": "ray.slakinski@gmail.com",
                     "name": "Ray Slakinski",
                     "uri": "http://www.slakinski.com"
                },
                 "sources": 
                [
                    "http://www.ospec.org"
                ],
                 "uri": "http://www.osync.org/posts/osync-launched",
                 "location": "Las Vegas, NV, USA",
                 "exeprt": "We lauched OSync today!",
                 "pub_date": "2009-08-05T11:17Z",
                 "tags": 
                [
                     "web",
                     "formats",
                     "specifications"
                ],
                 "attachments": 
                [
                    {
                         "hash": "6c6d81147f00bd6adb710d22bfe69f05",
                         "uuid": "25746ef0-b362-4d38-b4e6-a0443c634d7e",
                         "pub_date": "2009-08-05T11:17Z",
                         "explicit": false,
                         "uri": "http://www.osync.org/pcasts/osync-podcast-01.mp3",
                         "hash_type": "md5",
                         "filename": "osync-podcast-01.mp3",
                         "duration": 923282,
                         "type": "audio/mpeg",
                         "block": false,
                         "bytes": 228223
                    }
                ]
            }
        ],
    }

## Specification ##

### Main Elements ###

* uuid: Unique ID for the feed itself, great for using in conjunction with [SUP](http://code.google.com/p/simpleupdateprotocol/), [PubSubHubbub](http://code.google.com/p/pubsubhubbub/) or [rssCloud](http://rsscloud.org/)
* hub: A central place to see which oSync feeds have been updated. Usually a location for a servers [SUP](http://code.google.com/p/simpleupdateprotocol/), [PubSubHubbub](http://code.google.com/p/pubsubhubbub/) or [rssCloud](http://rsscloud.org/) location _(Optional)_
* title: Title of the feed
* subtitle: Subtitle for this feed _(Optional)_
* summary: A short description of this feed _(Optional)_
* uri: URI to where on this content came from
* language: Based on the [W3C standard language codes](http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes)
* copywrite: A string describing the copywrite for this feed
* copywrite_image: Image representation of copywrite, such as a [Creative Commons](http://creativecommons.org/) logo _(Optional)_
* location: A string containing either a text location such as "Oakville, Ontario, Canada" or latitude and longitude such as "43.437933,-79.754251" _(Optional)_
* pub_date: Date the feed was first published in [ISO 8601](http://en.wikipedia.org/wiki/ISO-8601) format example: 2009-08-05T11:17Z
* updated_date: Last time the feed was updated
* generator: What application/script created this output. Helpful for debugging. _(Optional)_
* tags: A list of tags/keywords/categories that you wish to associate with this feed _(Optional)_
* image: Should be a square .jpg image that is at least 600 x 600 pixels
* image_thumbnail: A thumbnail version (32x32) of the image in the 'image' key
* items: A list of items (see below for item description)

### Items ###

* uuid: Unique ID for this item
* title: title for this item
* uri: URI location of where to find this item
* sources: A list of sources for this item. Sites like digg.com might want to specify the original article here. _(Optional)_
* location: A string containing either a text location such as "Oakville, Ontario, Canada" or latitude and longitude such as "43.437933,-79.754251" _(Optional)_
* pub_date: Date item was first published in [ISO 8601](http://en.wikipedia.org/wiki/ISO-8601) format example: 2009-08-05T11:17Z
* updated_date: Last time the feed was updated
* summary: A short description of this item _(Optional)_
* body: The full text for this item
* author: Defines the author for this item (see below for description)
* contributors: a list of authors that also contributed to this item (see author description below) _(Optional)_
* tags: A list of tags/keywords/categories that you wish to associate with this item _(Optional)_
* attachments: A list of attached resources for this item (see below for description) _(Optional)_

#### Author ####

* name: Full name of the author
* uri: URI location of where you can find the author online
* email: E-Mail address of where you can contact the author _(Optional)_

#### Attachments ####

* uuid: Unique ID for this attachment
* filename: Allows you to specify a specific name for this file _(Optional)_
* uri: URI location of where to find this attachment
* pub_date: Date item was first published in [ISO 8601](http://en.wikipedia.org/wiki/ISO-8601) format example: 2009-08-05T11:17Z
* mime_type: [Mime-type](http://www.webmaster-toolkit.com/mime-types.shtml) that defines what type of attachment this is
* bytes: Attachment size in bytes
* duration: Duration in seconds, should be specified if type is audio or video _(Optional)_
* location: A string containing either a text location such as "Oakville, Ontario, Canada" or latitude and longitude such as "43.437933,-79.754251" _(Optional)_
* tags: A list of tags/keywords/categories that you wish to associate with this item _(Optional)_
* hash: [Hash for the file](http://www.electrictoolbox.com/article/linux-unix-bsd/howto-check-md5-file/). Hashes are useful to help the consumer that they downloaded the file correctly _(Optional)_
* hash_type: To be specified if hash is set and is not MD5 (MD5 is assumed) _(Optional)_
 * Note: Use lowercase (md5, sha256)
* explicit: Does the content contain explicit material? False if not specified _(Optional)_
* block: This should stop a consumer from showing this file in their UI. False if not specified _(Optional)_

<a rel="license" href="http://creativecommons.org/licenses/by-nd/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://creativecommons.org/images/public/somerights20.png" /></a>