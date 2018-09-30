# raw_rules
extract invalid raw-data based on the rule specified 

Briefly describe the conceptual approach you chose! What are the trade-offs?
The question is staright forward i beleive , just to validate the raw data 
here the approach i followed is to extract the rule in english into some hash value which will be eaisier to be used in the code 
which has been implemented in rueadrules.py by extracting some key words from each rule described 

What's the runtime performance? What is the complexity? Where are the bottlenecks?
Pefroamce will be mostly likely to depend the raw data and the set of rule described on same set of data 
Duration: 0.15 sec 
Complexity will be likely to be O(n), i am afriad if i am wrong , where n = total number of rules 

If you had more time, what improvements would you make, and in what order of priority?

1.isolating and grouping of rule would help more to analysie and retrive data when multiple rule applicable on same data 
2.similary grouping of rule/ raw_data will help in fliter them as per the rule 
3.Prioritising the rule handling first seems to handle more complex data as well 


Thanks,
Ibrahim Sha.K.A