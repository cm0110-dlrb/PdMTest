const dbx = process.env.sl.BrZj6-TQVT68AHJ2Z5YBBtK7Pw6uyQCRO9SaOGcGa0RYdM5VK22yoyh60M1O7_k7zKeFKLTOtIbQnoQh8E2PtfXMtPFKVsEoVGWXx-292TYPiJ1P3JKm_-tU7juBUhmGOMeje9Y4_ll23_rzBrtr;
dbx.usersGetCurrentAccount()
 .then(response => {
    console.log(response);
 })
 .catch(error => {
    console.error(error);
 });