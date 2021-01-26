import React, { useState, useEffect } from 'react';
import Table from './Table'
import Form from './Form';
import axios from 'axios';

function MyApp() {
   const [characters, setCharacters] = useState([]);

   function updateList(person) { 
      makePostCall(person).then( result => {
      if (result.status == 201) //task 1?
         setCharacters([...characters, result.data] );
      });
   }

   async function makePostCall(person){
      try {
         const response = await axios.post('http://localhost:5000/users', person);
         return response;
      }
      catch (error) {
         console.log(error);
         return false;
      }
   }

   async function fetchAll(){
      try {
         const response = await axios.get('http://localhost:5000/users');
         return response.data.users_list;     
      }
      catch (error){
         //We're not handling errors. Just logging into the console.
         console.log(error); 
         return false;         
      }
   }

   useEffect(() => {
      fetchAll().then( result => {
         if (result)
            setCharacters(result);
       });
   }, [] );

   /*function removeOneCharacter (index) {
      const updated = characters.filter((character, i) => {
         return i !== index
      });
      setCharacters(updated);
   }*/

   async function removeOneCharacter (index) {
      try {
         const response = await axios.delete('http://localhost:5000/users/' + characters[index]._id);
         if (response.status == 204)
         {
            const updated = characters.filter((character, i) => {
               return i !== index
            });
            setCharacters(updated);
         }
      }
      catch (error){
         //We're not handling errors. Just logging into the console.
         console.log(error); 
         return false;         
      }
   }

   return (
      <div className="container">
        <Table characterData={characters} removeCharacter={removeOneCharacter} />
        <Form handleSubmit={updateList} />
      </div>
   ) 
}

export default MyApp;