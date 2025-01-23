all:
	xxd -i site/index.html > html.c

	@cmake -G Ninja -B build -S . -D CMAKE_BUILD_TYPE=Release
	@cmake --build build

	strip ./build/bin/example
	./build/bin/example

clean:
	@rm -rf build
