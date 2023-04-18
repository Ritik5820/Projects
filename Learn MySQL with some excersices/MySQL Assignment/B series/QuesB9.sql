-- B9 What is trigger and how to Create a Trigger in SQL ?

-- Triggers are the codes that are executed automatically in response to certain events on a particular table. For eg: If the HR wants to send the welcome mail to 
-- every new commers the HR wouldn't do it manually. He would create a trigger that will automatically send the mails to the new commers.

create trigger trigger_name
(before | after)
[Insert|Update|Delete]
on table_name
[for each row|for each column]
[trigger body]