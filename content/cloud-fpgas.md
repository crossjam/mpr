Title: Cloud FPGAs
Date: 2017-06-12 20:39
Author: crossjam
Category: Uncategorized
Slug: cloud-fpgas
Status: published

[FPGA][2] stands for Field-Programmable Gate Array *(sic)*. I was struck by this article from [The New Stack][3] summarizing ways [FPGAs can be incorporated into cloud computing offerings][1].

> The array of gates that make up an FPGA can be programmed to run a specific algorithm, using the combination of logic gates (usually implemented as lookup tables), arithmetic units, digital signal processors (DSPs) to do multiplication, static RAM for temporarily storing the results of those computation and switching blocks that let you control the connections between the programmable blocks. Some FPGAs are essentially systems-on-a-chip (SoC), with CPUs, PCI Express and DMA connections and Ethernet controllers, turning the programmable array into a custom accelerator for the code running on the CPU.

> The combination means that FPGAs can offer massive parallelism targeted only for a specific algorithm, and at much lower power compared to a GPU. And unlike an application-specific integrated circuit (ASIC), they can be reprogrammed when you want to change that algorithm (that’s the field-programmable part).

Give the article a read to hear about how Microsoft is using FPGAs to accelerate network packet processing for software defined networking, SDN, applications. FPGAs have always seemed to only be applicable in really niche, vertical applications, but this feels like a relatively broad use case to me. Also, a number of other really important verticals (crypto, *omics) along with potential to join in the AI hype wave would seem to make for a bright FPGA future. The “hardware microservices” portmanteau is a good soundbite.

FPGA programming has always been extremely difficult. I’m surprised that tightly integrated programming stacks haven’t emerged to make this a lot easier, given the relatively high value they would seem to bring. The article does hint at this potential future though. Alternatively, one can look at cloud APIs as eventually becoming the “programming stack” that many developers use to exploit FPGAs.

Feels like a trend to keep an eye on.

[1]: https://thenewstack.io/developers-fpgas-cloud/
[2]: https://en.wikipedia.org/wiki/Field-programmable_gate_array
[3]: https://thenewstack.io/