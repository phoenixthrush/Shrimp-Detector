all:
	mkdir -p src/build/
	cd src && xxd -i site/index.html > html.c
	cd src && cmake -G Ninja -B build -S . -D CMAKE_BUILD_TYPE=Release
	cd src && cmake --build build
	cd src && strip ./build/bin/shrimp
	cd src && ./build/bin/shrimp

clean:
	cd src && rm -rf build
