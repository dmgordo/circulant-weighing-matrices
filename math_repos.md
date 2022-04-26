# Combinatorial Databases #

In late 2021 Robert Craigen started a discussion with a number of
researchers in "Hadamardish orthogonal stuff in combinatorics" about
the need for a "more systematic, comprehensive and permanent reference
system for matrices, sequences, and all sorts of miscellany pertaining
to Hadamard matrices and the various generalizations, variations and
spin-offs".  The discussions identified a large number of existing
online repositories with wildly different implementations and user interfaces, but no one
path forward.

This book is the result of an extended investigation of options.  It
may or may not turn out to be a good way to proceed,
but gives one possible step towards
Craigen's goals, and will hopefully help push the discussion forward.


## Mathematical Repositories, a very brief history ##

The oldest known mathematical data repository may be a 4500 year-old tablet from the
Sumerian city of Shuruppag.  See {cite}`campbell2003history` for a
history of mathematical table making over the millenia, through logarithm,
actuarial and astronomical tables up to spreadsheets.

For most of the 20th century, mathematical data was published either
in book form (for example {cite}`hcd`) or as microfiche supplements to journal articles.
Later, online repositories began to appear, but were often scattered in
different places, often made by people without knowledge of other
overlapping material.
URLs often changed, leaving broken links behind.
Finding and categorizing everything available on a given subject can be
challenging; see for example {cite}`swain2020survey` for a thorough examination of
graph theory sites, and
{cite}`bervcivc2020discretezoo` 
and {cite}`fevola2022mathematical`
and their associated repositories
[DiscreteZoo](https://github.com/DiscreteZOO) and 
[MathRepo](https://matherepo.mis.mpg.de)
for a look at some different types of
online mathematical databases aspiring to FAIRness.

Many other STEM areas, such as biology, geophysics and
crystallography, routinely deal with large datasets, and so are far
ahead of mathematics in adapting to new options for presenting their
data.  In 2014 the Joint Declaration of Data Citation Principles laid
out principles for data citation, and papers such as
{cite}`starr2015achieving` and {cite}`fenner2019data` gave roadmaps
for achieving these principles.

There are a number of large initiatives aimed at advancing the handling of data in
mathematics, largely in Europe.  <a
href="opendreamkit.org">OpenDreamKit</a> (Open Digital Research
Environments Toolkit for the Advancement of Mathematics) ran from 2015
to 2019.  MaRDI, the <a href="https://mardi4nfdi.de/">Mathematical Research
Data Initiative</a>, is a German initiative that started in 2021.


## FAIR Data ##

In recent years the importance of making research data in all areas of
science and technology available has been recognized as crucial, 
resulting in the FAIR data principles: data should be:

* Findable
* Accessible
* Interoperable
* Reusable

These guiding principles were detailed in {cite}`fairprinciples`:
   
To be Findable:   
F1. (meta)data are assigned a globally unique and persistent identifier  
F2. data are described with rich metadata (defined by R1 below)   
F3. metadata clearly and explicitly include the identifier of the data it describes   
F4. (meta)data are registered or indexed in a searchable resource   

To be Accessible      
A1. (meta)data are retrievable by their identifier using a standardized communications protocol   
    A1.1. the protocol is open, free, and universally implementable   
    A1.2. the protocol allows for an authentication and authorization procedure, where necessary   
A2. metadata are accessible, even when the data are no longer available   

To be Interoperable:   
I1. (meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation.   
I2. (meta)data use vocabularies that follow FAIR principles   
I3. (meta)data include qualified references to other (meta)data   

To be Reusable:   
R1. meta(data) are richly described with a plurality of accurate and relevant attributes   
    R1.1. (meta)data are released with a clear and accessible data usage license   
    R1.2. (meta)data are associated with detailed provenance   
    R1.3. (meta)data meet domain-relevant community standards   


This paper {cite}`BKR20` looks at how FAIR data principles apply to
mathematical data, and propose a further principle they call "deep
FAIR" data, and give a sampling of datasets <a href="https://data.mathhub.info/">here</a>.

In the next sections we discuss what these principles mean in the
context of combinatorial data repositories, and how they influence the
design choices of this book.

### Findable

There are many online repositories of mathematical data, but locating
them can be difficult, and often links are broken when a website has
moved or just disappeared.  So establishing a permanent location is
critical.

GitHub is one place that code and data can be deposited, but it is not
designed for permanent preservation.  A number of repositories that
are designed to be permanent and discoverable are available, such as 
[Dryad](https://datadryad.org/stash/),
[Figshare](https://figshare.com),
and [Zenodo](https://zenodo.org/).
They all assign a record a DOI
(Digital Object Identifier), by which it can be uniquely identified and located.  

They have various pros and cons, and new
ones are regularly appearing.  I decided to go with a GitHub repo
archived at Zenodo.

Note that the author's website {cite}`ljcr` still exists, and provides
a friendlier interface for users who only need a few of its
combinatorial objects.  For now this book is a supplement, but the
long-term plan is for it, and others for difference sets, covering designs and
Steiner systems, to replace it entirely.


Adding metadata so that tools like Google Dataset Search can find the
repository is important.  There are also directories of research data
repositories, such as <https://www.re3data.org> and 
<https://fairsharing.org>.  Making this data findable is still a work
in progress.

### Accessible

How to present data is another question.  Jupyter Notebooks are a way
to present data and code together, so that a user can quickly
manipulate it.  Jupyter books are a way to add material beyond the
notebook.
In {cite}`sokol2021you` a Jupyter Book is used to prepare data, a
paper, and slides for a talk all in one package.

One way to interact with a Jupyter book is to install the Jupyter Book
software, the source for the book itself, and then build it.  See
{cite}`executable_books_community_2020_4539666` 
for information about how to do that.

That's more work than most casual users will be willing to do.  An
easier alternative is to use <a href="https://mybinder.org">BinderHub</a>,
which can be set up to execute a Jupyter Book on GitHub.  See
the <i>Launch into interactive computing interfaces</i> section of 
{cite}`executable_books_community_2020_4539666`.
Click on the launch button above to try it out.


### Interoperable

Presenting the data as a CSV file seemed like the most direct
approach.  Simple Python code is included to do basic processing,
so that the data can be examined without additional work, and 
can be used with other people's code with a minimum of effort.

The goal was to keep the data and code as simple as possible.  This
dataset is fairly small, which is why it was chosen to start with.
The covering designs database is several gigabytes.  That amount of
space is not a problem, but putting it all in a Jupyter Notebook and
getting good performance may be more challenging.


### Reusable

When you store your data on a repository, you will need to specify a
license for use.  Creative Commons has a number of options:

* CC BY: reuse is allowed, but must cite the creators
* CC NC: no commercial use
* CC0: nearly public domain

This paper In {cite}`labastida2020licensing` looks at questions about
sharing research data.  
These workshop slides {cite}`goodbadugly` give a good overview of the
steps and options involved in publishing research data.

This book and its data are released under the
CC BY license.  


