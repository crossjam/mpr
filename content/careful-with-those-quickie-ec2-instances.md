Title: Careful With Those Quickie EC2 Instances
Date: 2011-07-07 20:53
Author: crossjam
Category: Uncategorized
Slug: careful-with-those-quickie-ec2-instances
Status: published
Attachments: wp/mpr/wp-content/uploads/2011/07/EBS-EC2-AMI.png

<div style="text-align:center;"><img src="http://crossjam.net/wp/mpr/wp-content/uploads/2011/07/EBS-EC2-AMI.png" alt="EBS EC2 AMI" border="0" width="442" height="75" style="margin: 10px;"/></div>

So I was noodling around with [Amazon EC2][1] a few days ago. I used one of their quick start Linux machine images for about 10 minutes, then terminated the instance. Afterwards, I noticed I had some EBS volumes that were terminating also.

This is a complete *noob* lesson, but some AMIs use EBS volumes for their root disk instead of loading from S3. Thus the unexpected EBS volume. Operator error, please [read the fine print][2].

It's not a huge deal, although you could inadvertently incur costs with an EBS volume, since they're metered by I/O operations in addition to storage. I'm assuming Amazon pays for the storage on these volumes but the user forks over for the ops.

[1]: http://aws.amazon.com/ec2/
[2]: http://aws.amazon.com/ec2/faqs/#What_is_the_difference_between_using_the_local_instance_store_and_Amazon_Elastic_Block_storage_for_the_root_device