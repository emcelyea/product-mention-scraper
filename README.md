# product-mention-scraper
Testing a scraper for keyword mentions on reddit

### Considerations
The ideal performance would be a user types in a keyword (i.e. spiderman) and a list of every occurence is returned.
This is untenable for a few reasons:
* Reddit API does not support this behavior natively, it is effective for recent searches over specific subreddits, but not historical searches.
* Reddit generates 25+ billion comments a month, that is > 23 GB per month of text, an exhaustive search for all the years would be tricky.

So we have two problems that we can solve in two different ways:
* To check historical mentions we can pull all the comments as a zip from [reddit comment history](https://files.pushshift.io/reddit/comments/). This could be impractical but we can check the viability of storing terabytes of text and grepping it.
* To check recent mentions we can leverage the reddit API


