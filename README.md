# vkLineChat
Simple chat based on vk.com API

In current version it's able to view list of your unread dialogs at vk.com and answer them or leave unread. 

So it works the next way :

	1)'Try to continue old session? [y/n] : ' 
	
		y) try to read date from file "auth_content", in case of error print it and go to 1->n) 
        
	        n) get access token from vk.com and write it into file "auth_content" 
        
	2)Show you all your unread dialogs, if they exist. 

	3)Ask you 'Do you want to see any of this dialogs? [y/n]:' 

        	y) Ask 'Select number of dialog or '-1' to cancel: ' 
        
                	#) view chosen dialog (all unread messages and 7 additional) 
                
                	'Do you want to answer?[y/n] ' 
                
                        	y) take your input and send it 
                        
                        	n) #skip 
                        
                	Ask 'Do you want to mark messages as read?[y/n] ' 
                
                        	y) Ask 'How many messages do want to leave unread? : ' 
                        
                        	take you input(№) and leave № unread messages in the and of you dialog 
                        
                        	n) #skip 
                        
                	-1) go to 3->n 
                
        	n) #skip  
        
	4)Bye...Bye... 

