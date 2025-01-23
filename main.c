#include "webview/webview.h"
#include <stddef.h>
#include "html.c"

#ifdef _WIN32
#include <windows.h>
#endif

#ifdef _WIN32
int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrevInst, LPSTR lpCmdLine,
                   int nCmdShow)
{
    (void)hInst;
    (void)hPrevInst;
    (void)lpCmdLine;
    (void)nCmdShow;
#else
int main(void)
{
#endif
    webview_t w = webview_create(0, NULL);
    webview_set_title(w, "Shrimp Detector");
    webview_set_size(w, 700, 500, WEBVIEW_HINT_FIXED);
    webview_set_html(w, (const char *)site_index_html);
    webview_run(w);
    webview_destroy(w);
    return 0;
}
