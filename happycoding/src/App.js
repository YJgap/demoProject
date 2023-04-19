import React, { useState, useEffect } from "react";
import axios from "axios";
// import "bootstrap/dist/css/bootstrap.min.css";
import Background from "./Background";

function App() {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    const fetchContacts = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:5158/read");
        setContacts(response.data);
      } catch (error) {
        console.error("Error fetching contacts:", error);
      }
    };

    fetchContacts();
  }, []);

  const updateContact = async (index, field, value) => {
    const updatedContacts = [...contacts];
    updatedContacts[index][field] = value;
    setContacts(updatedContacts);

    // 서버에 업데이트된 정보를 전송합니다.
    try {
      const response = await axios.post("http://127.0.0.1:5158/update", {
        id: contacts[index].id,
        firstName: contacts[index].firstName,
        lastName: contacts[index].lastName,
        nickName: contacts[index].nickName,
        phone: contacts[index].phone,
        memo: contacts[index].memo,
      });

      if (!response.data.success) {
        console.error("Contact update failed");
      }
    } catch (error) {
      console.error("Error updating contact:", error);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-green-400 to-blue-500 text-3xl">
      <Background />
      <div className="container mx-auto p-4">
        <h1 className="text-6xl font-bold text-black my-8">전화번호부</h1>
        <div className="bg-white rounded shadow p-6">
          {contacts.map((contact, index) => (
            <div key={contact.id} className="border-b py-4">
              <div className="grid grid-cols-2 gap-4" class="text-black-200">
                <input
                  type="text"
                  className="border rounded w-full py-2 px-3"
                  value={`${contact.firstName} ${contact.lastName}`}
                  onChange={(e) => {
                    const [firstName, lastName] = e.target.value.split(" ");
                    updateContact(index, "firstName", firstName);
                    updateContact(index, "lastName", lastName);
                  }}
                />
                <input
                  type="text"
                  className="border rounded w-full py-2 px-3"
                  value={contact.phone}
                  onChange={(e) =>
                    updateContact(index, "phone", e.target.value)
                  }
                />
              </div>
              <div className="mt-2">
                <input
                  type="text"
                  className="border rounded w-full py-2 px-3"
                  placeholder="메모 추가"
                  value={contact.memo}
                  onChange={(e) => updateContact(index, "memo", e.target.value)}
                />
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
