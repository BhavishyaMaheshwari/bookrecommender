const loader = `
            <li role="status" class='flex items-center justify-center'>
                <svg aria-hidden="true" class="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
                </svg>
                <span class="sr-only">Loading...</span>
            </li>
        `;

const addToFavorites = (id) => {
  const newFavs = window.localStorage.getItem("favorites")
    ? window.localStorage.getItem("favorites").split(",").concat(id)
    : [id];

  window.localStorage.setItem("favorites", newFavs);
  window.alert("Added to favorites!!!");
};

const removeFromFavorites = (id) => {
  if (!window.localStorage.getItem("favorites")) return;
  const prevFavs = window.localStorage.getItem("favorites").split(",");
  const newFavs = prevFavs.filter((fav) => fav.trim() !== id);
  window.localStorage.setItem("favorites", newFavs);
  window.location.reload()
};

const addToLikes = (id) => {
  const newFavs = window.localStorage.getItem("likes")
    ? window.localStorage.getItem("likes").split(",").concat(id)
    : [id];

  window.localStorage.setItem("likes", newFavs);
  window.alert("Added to likes!!!");
};

const removeFromLikes = (id) => {
  if (!window.localStorage.getItem("likes")) return;
  const prevFavs = window.localStorage.getItem("likes").split(",");
  const newFavs = prevFavs.filter((fav) => fav.trim() !== id);
  window.localStorage.setItem("likes", newFavs);
  window.location.reload()
};

const displayFavOrLikes = (data) => {
  resultBox.innerHTML = "";
  likes = window.localStorage.getItem("likes")
    ? window.localStorage.getItem("likes").split(",")
    : [];
  favorites = window.localStorage.getItem("favorites")
    ? window.localStorage.getItem("favorites").split(",")
    : [];
  data.forEach((book) => {
    const bookItem = document.createElement("li");
    bookItem.setAttribute("class", "my-2");
    bookItem.innerHTML = `
                    <div class="flex border-b-2 py-2">
                        <img class="w-[180px] h-[180px] object-contain" src="${
                          book.volumeInfo["imageLinks"]
                            ? book.volumeInfo.imageLinks.smallThumbnail
                            : "/static/img-nf.png"
                        }" alt="${book.volumeInfo.title}">
                        <div class="flex flex-1 justify-start relative">
                            <div class="content flex-1 relative">
                                <h2 class="font-semibold text-[25px] leading-none text-wrap max-w-[80%]">${
                                  book.volumeInfo.title
                                }</h2>
                                <p class="font-medium text-[15px] text-[#464646] mb-2">${book.volumeInfo.authors.join(
                                  ", "
                                )}</p>
                                <div class="flex gap-1 flex-wrap">
                                    ${
                                      book.volumeInfo["categories"]
                                        ? book.volumeInfo.categories
                                            .map(
                                              (category) =>
                                                `<span class="bg-pink-500 rounded-[10pc] px-[9px] py-[2px] text-[13px] text-white">${category}</span>`
                                            )
                                            .join("")
                                        : `<span class="bg-red-500 rounded-[10pc] px-[9px] py-[2px] text-[13px] text-white">No Category Found</span>`
                                    }
                                </div>
                                <p class="text-[15px] mt-2">${
                                  book.volumeInfo.description
                                    ? book.volumeInfo.description.slice(0, 150) +
                                      "..."
                                    : "No Description"
                                }</p>
                                <div class="flex gap-2 mt-2">
                                    <button 
                                        class="flex items-center gap-2 bg-blue-500 px-4 py-2 text-white rounded-md hover:bg-blue-600"
                                        onclick=${
                                          likes.includes(book.id)
                                            ? `removeFromLikes('${book.id}')`
                                            : `addToLikes('${book.id}')`
                                        }
                                    >
                                        <i class="fa ${
                                          likes.includes(book.id)
                                            ? "fa-heart"
                                            : "fa-heart-o"
                                        }" aria-hidden="true"></i>
                                        Like
                                    </button>
                                    <button 
                                            class="flex items-center gap-2 bg-pink-500 px-4 py-2 text-white rounded-md hover:bg-pink-600"
                                            onclick=${
                                              favorites.includes(book.id)
                                                ? `removeFromFavorites('${book.id}')`
                                                : `addToFavorites('${book.id}')`
                                            }
                                        >
                                            <i class="fa ${
                                              favorites.includes(book.id)
                                                ? "fa-bookmark"
                                                : "fa-bookmark-o"
                                            }" aria-hidden="true"></i>
                                            Read Later
                                        </button>
                                </div>
                            </div>
                            <div class="absolute top-0 right-1 flex gap-2">
                                ${
                                  book['customBook'] ? `
                                    <a href="${book['volumeInfo']['infoLink']}" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 bg-gray-200 w-[40px] h-[40px] text-white rounded-[50%] hover:bg-gray-300" >
                                    <i class="fa-solid fa-link text-black"></i>
                                  </a>
                                ` : `<a href="${
                                  book.accessInfo.webReaderLink
                                }" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 bg-gray-200 w-[40px] h-[40px] text-white rounded-[50%] hover:bg-gray-300" >
                                    <i class="fa-brands fa-google-play text-black"></i>
                                </a>
                                <a href="${
                                  book.volumeInfo.infoLink
                                }" target="_blank" rel="noopener noreferrer" class="flex items-center justify-center gap-2 bg-gray-200 w-[40px] h-[40px] text-white rounded-[50%] hover:bg-gray-300" >
                                    <i class="fa-solid fa-book text-black"></i>
                                </a>`
                                }
                                
                            </div>
                            
                            
                        </div>
                    </div>
            `;
    resultBox.appendChild(bookItem);
  });
};
