
$(document).ready(function () {

    function getProducts(productFilters, filterName) {
      let url = "http://127.0.0.1:8000/api/products/";

        console.log(filterName, productFilters);

        if (filterName === 'category' && productFilters.length > 0) {
            url += "?category=" + productFilters.join(",");
        }

        if (filterName === 'brand' && productFilters.length > 0) {
            url += "?brand=" + productFilters.join(",");
        }

        if (filterName === 'seller' && productFilters.length > 0) {
            url += "?seller=" + productFilters.join(",");
        }

        if (filterName === 'warranty' && productFilters.length > 0) {
            url += "?warranty=" + productFilters.join(",");
        }

        if (filterName === 'discount' && productFilters.length > 0) {
            url += "?discount=" + productFilters.join(",");
        }

      axios
          .get(url)
          .then(function (response) {
              let products = Object.values(response.data);
                var filteredProducts = filterProducts(products, productFilters, filterName);


          displayProducts(filteredProducts);
        })
        .catch(function (error) {
          console.log(error);
        });
      }

      // Function to filter products based on category
    function filterProducts(products, productFilters, filterName) {
      if (productFilters.length === 0) {
        return products; // No filters applied, return all products
      }

        if (filterName === 'category') {
            return products.filter(function (product) {
                return productFilters.includes(product.category[0].name);
                });
        }
        if (filterName === 'brand') {
            return products.filter(function (product) {
                return productFilters.includes(product.brand.name);
                });
        }
        if (filterName === 'seller') {
            return products.filter(function (product) {
                return productFilters.includes(product.seller.name);
                });
        }
        if (filterName === 'warranty') {
            return products.filter(function (product) {
                return productFilters.includes(product.warranty.value+'-'+product.warranty.time);
                });
        }

        return products.filter(function (product) {
            return productFilters.includes(product.discount.name);
            });

    }

    // Function to display the retrieved products
    function displayProducts(products) {
      var productList = $('#product-list');
      productList.empty();
      products.forEach((element) => {
        let item = `
                      <div class="card mx-3 my-3" id="card-item-${element.id}" style="width: 18rem;">
                      <img class = "product_img" src="${element.image}" class="card-img-top" alt="...">
                      <div class="card-body">
                          <h3 class="card-title">${element.name}</h3>
                          <h6 class="card-title">${element.brand.name}</h6>
                          <p class="card-text">${element.price}</p>
                          <p class="card-text">${element.discount.value} % off</p>
                          <a href="#" class="btn btn-primary">Details</a>
                      </div>
                      </div>
                  `;
        productList.append(item);
      });
      }


  // Event listener for category checkbox changes
    $(".form-check-category").change(function () {
      var categoryFilters = [];
      $(".form-check-category:checked").each(function () {
        categoryFilters.push($(this).val());
      });

      getProducts(categoryFilters, 'category');
    });

  // Event listener for brand checkbox changes
    $(".form-check-brand").change(function () {
      var brandFilters = [];
      $(".form-check-brand:checked").each(function () {
        brandFilters.push($(this).val());
      });

      getProducts(brandFilters, 'brand');
    });

    // Event listener for seller checkbox changes
    $(".form-check-seller").change(function () {
      var sellerFilters = [];
      $(".form-check-seller:checked").each(function () {
        sellerFilters.push($(this).val());
      });

      getProducts(sellerFilters, 'seller');
    });

    // Event listener for Discount checkbox changes
    $(".form-check-discount").change(function () {
      var discountFilters = [];
      $(".form-check-discount:checked").each(function () {
        discountFilters.push($(this).val());
      });

      getProducts(discountFilters, 'discount');
    });

    // Event listener for Warranty checkbox changes
    $(".form-check-warranty").change(function () {
      var warrantyFilters = [];
      $(".form-check-warranty:checked").each(function () {
        warrantyFilters.push($(this).val());
      });

      getProducts(warrantyFilters, 'warranty');
    });

    getProducts([], 'none');

  });
