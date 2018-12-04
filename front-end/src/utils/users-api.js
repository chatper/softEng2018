import axios from 'axios';

const http = axios.create({
  baseURL: 'http://localhost:8080/api/v1.0/',
  timeout: 5000,
});

function getUsers() {
  return http.get('users').then(response => response.data);
}

function getUser(id) {
  const url = `users/${id}`;
  return http.get(url).then(response => response.data);
}

function loginUser(data) {
  return http.post('users/login', data).then(response => response.data);
}

function registerUser(data) {
  return http.post('users', data).then(response => response.data);
}

function deleteUser(data) {
  const url = `users/${data.id}`;
  return http.delete(url, data).then(response => response.data);
}

function updateUser(data) {
  const url = `users/${data.id}`;
  return http.put(url, data).then(response => response.data);
}

export { getUsers, getUser, loginUser, registerUser, deleteUser, updateUser };
