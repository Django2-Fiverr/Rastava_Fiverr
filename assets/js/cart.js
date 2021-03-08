

var updateBtns = document.querySelectorAll('.update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var gigId = this.dataset.gig
		var action = this.dataset.action
		console.log('gigId:', gigId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(gigId, action)
		}else{
			updateUserOrder(gigId, action)
		}
	})
}

function updateUserOrder(gigId, action){
	console.log('User is authenticated, sending data...')

		// var url = '//'

		fetch('/gigs/update_item/', {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'gigId':gigId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

// function addCookieItem(productId, action){
// 	console.log('User is not authenticated')

// 	if (action == 'add'){
// 		if (cart[productId] == undefined){
// 		cart[productId] = {'quantity':1}

// 		}else{
// 			cart[productId]['quantity'] += 1
// 		}
// 	}

// 	if (action == 'remove'){
// 		cart[productId]['quantity'] -= 1

// 		if (cart[productId]['quantity'] <= 0){
// 			console.log('Item should be deleted')
// 			delete cart[productId];
// 		}
// 	}
// 	console.log('CART:', cart)
// 	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
// 	location.reload()
// }