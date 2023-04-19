// Users.js를 이것으로 대체
import React, { useState, useEffect } from "react";
import axios from "axios";

function Users() {
  const [contacts, setContacts] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        // 요청이 시작 할 때에는 error 와 users 를 초기화하고
        setError(null);
        setContacts(null);
        // loading 상태를 true 로 바꿉니다.
        setLoading(true);
        const response = await axios.get("http://127.0.0.1:5158/read");
        setContacts(response.data); // 데이터는 response.data 안에 들어있습니다.
      } catch (e) {
        setError(e);
      }
      setLoading(false);
    };

    fetchUsers();
  }, []);

  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러가 발생했습니다</div>;
  if (!contacts) return null;
  return (
    <ul>
      {contacts.map((contact) => (
        <li key={contact.id}>
          {contact.userfirstName} ({contact.firstName}){contact.userlastName} (
          {contact.lastName}){contact.userphone} ({contact.phone})
        </li>
      ))}
    </ul>
  );
}
export default Users;
