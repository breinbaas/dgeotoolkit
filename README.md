### DGeoToolkit

DGeoToolkit is a package that supports the creation / automation of Deltares DStability and DGeoFlow input files
and calculations. It is loosely based on Deltares geolib but tries to be minimalistic, levee based and will 
**not** support other (older) Deltares software (if DSettlement is updated we plan to support that as well).

### The question that might be on your mind

**Why another package if we have geolib?**

The main reason is that the code in geolib is quite complicated because it serves multiple software packages,
some of which with the old file structure, some with the new. DGeoToolkit will focus on DStability,
DGeoFlow and (the to be released) DSettlement which are the main packages needed for levee assessments.

The code in this repo tries to be minimalistic and easy / easier to maintain. It will also focus on
things that are currently not possible with geolib like complicated geometry adjustments. 

### Supported files

* stix from version 2023.01 and up (use the convertor tool provided by Deltares to update old stix files)
* [TODO] dgeoflow files
* [TODO] dsettlement files (only new version which is under development now)

### Support me

You can join the development team or support me by hiring me to write code or focus on code you need, contact
me using breinbaasnl@gmail.com

Rob van Putten | breinbaasnl@gmail.com | 2023

