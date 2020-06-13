Title: Serverless on k8s
Date: 2018-05-18 17:10
Author: crossjam
Category: Uncategorized
Slug: serverless-on-k8s
Status: published

So great, you’ve got your Raspberry Pi Kubernetes cluster up and running. Now what? Luckily, the k8s ecosystem seems to be supporting three different approaches to low friction, “serverless” computing-style deployment of application. It’s nice to have choice, but sometimes a little advice helps.

Enter [Hisham Hasan of Rancher, to explain the trio][1] of [OpenFaas][2], [Kubeless][3], and [Fission][4]:

> This whitepaper will explore how we can take the very useful design parameters and service orchestration features of K8s and marry them with serverless frameworks and Functions as a Service (FaaS). In particular, we will hone in on the features and functionalities, operational performance and efficiencies of three serverless frameworks that have been architected on a K8s structure: (i) Fission; (ii) OpenFaaS; and (iii) Kubeless.

The nice thing about Hasan’s blog post is that it gets into the deployment details of each toolkit. This is good to understand in addition to the developer experience that each platform provides. Clear contrasts can be seen, and now I have a better understanding of where the pain points might emerge.

[1]: https://rancher.com/blog/2018/2018-04-23-evaluation-of-serverless-frameworks-for-kbe/
[2]: https://www.openfaas.com/
[3]: https://kubeless.io/
[4]: https://fission.io/