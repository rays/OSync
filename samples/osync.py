import simplejson

osync_sample = {
    'uid': 'osync-news-blog', # unique ID for the feed itself, great for using with SUP http://code.google.com/p/simpleupdateprotocol/
    'title': 'News about OSync',
    'subtitle': 'Content Syndcation via JSONP',
    'summary': 'All the news you can use about your favorite new web syndication format OSync',
    'uri': 'http://www.osync.org',
    'language': 'en', # Based on the W3C standard http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
    'copywrite': 'Creative Commons Attribution-Noncommercial-No Derivative Works 3.0',
    'location': 'Oakville, Ontario, Canada', # either text or lat&lng (Optional)
    'pub_date': '2009-08-05T11:17Z', #ISO 8601 http://en.wikipedia.org/wiki/ISO-8601
    'updated_date': '2009-08-05T12:17Z',
    'generator': 'TextMate http://macromates.com/', # What application/script created this output. Helpful for debuggging.
    'tags': [ # A set of tags/keywords/categories that you wish to associate with this feed
                'web',
                'formats',
                'specifications',
            ],
    'image': 'http://www.osync.org/media/osync-600x600.jpg', # Should be a square .jpg images that are at least 600 x 600 pixels
    'thumbnail': 'http://www.osync.org/media/osync-32x32.jpg', # A thumbnail version (32x32) of the image in the 'image' key
    'items': [
                {
                    'uid': 'http://www.osync.org/posts/osync-launched',
                    'title': 'OSync Launched!',
                    'link': 'http://www.osync.org/posts/osync-launched',
                    'sources': [ # Optional, a list of sources for this item. Sites like digg.com might want to specifiy the original article here.
                                    'http://www.ospec.org',
                               ],
                    'location': '43.459679,-79.666414',
                    'pub_date': '2009-08-05T11:17Z',
                    'updated_date': '2009-08-05T11:17Z',
                    'author': {
                                'name': 'Ray Slakinski',
                                'uri': 'http://www.slakinski.com',
                                'email': 'ray.slakinski@gmail.com', # Optional
                              },
                    'tags': [ # A set of tags that you wish to associate with this item
                                'web',
                                'formats',
                                'specifications',
                            ],
                    'exeprt': 'We lauched OSync today!',
                    'body': 'We lauched OSync today! we had a big party and it was all kinds of fun. I hope you like it!',
                    'attachments': [
                                        {
                                            'uid': '6c6d81147f00bd6adb710d22bfe69f05',
                                            'filename': 'osync-podcast-01.mp3', # Optional, allows you to specify a specific name for this file.
                                            'uri': 'http://www.osync.org/pcasts/osync-podcast-01.mp3', # usually http or https
                                            'pub_date': '2009-08-05T11:17Z',
                                            'type': 'audio/mpeg', # Use valid mime-types to define what type of attachment this is
                                            'size': 228223,
                                            'duration': 923282, # Optional, durination in seconds
                                            'location': '43.459679,-79.666414',
                                            'hash': '6c6d81147f00bd6adb710d22bfe69f05', # Optional hash for the file
                                            'hash_type': 'md5', # needs to be specified if hash is set, should specify the algorythm used
                                            'explicit': False, # Does the content contain explicit material? (Optional, False if not specified)
                                            'block': False, # Optional, this should stop a consumer from showing this file in their UI
                                        },
                                        {
                                            'uid': 'dfb421284dbdbaba7723bb9d32f63f0d',
                                            'filename': 'party1.jpg',
                                            'uri': 'http://www.osync.org/images/party1.jpg',
                                            'pub_date': '2009-08-05T11:17Z',
                                            'type': 'image/jpeg',
                                            'size': 34000,
                                            'location': '43.459679,-79.666414',
                                            'hash': 'dfb421284dbdbaba7723bb9d32f63f0d',
                                            'hash_type': 'md5',
                                            'tags': [
                                                        'osync',
                                                        'party',
                                                    ],
                                        },
                                        {
                                            'uid': '288f7766e5653b8dd5b5faa17d08a0fe',
                                            'filename': 'party2.jpg',
                                            'uri': 'http://www.osync.org/images/party2.jpg',
                                            'pub_date': '2009-08-05T11:17Z',
                                            'type': 'image/jpeg',
                                            'size': 73000,
                                            'location': '43.459679,-79.666414',
                                            'hash': '288f7766e5653b8dd5b5faa17d08a0fe',
                                            'hash_type': 'md5',
                                            'tags': [
                                                        'osync',
                                                        'party',
                                                    ],
                                        },
                                   ],
                },
            ],
}

print simplejson.dumps(osync_sample)