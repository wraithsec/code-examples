#include <argp.h>
#include <stdio.h>

const char *argp_program_version = "Test v123";
const char *argp_program_bug_address = "Listen@Fairydust.com";
static char doc[] = "Testing out c code by counting to a chosen number!";
static char args_doc[] = "[FILENAME] . . .";
static struct argp_option options[] = {
    {"count", 'c', 0, 0, "Number to count to!"},
    { 0 }
};

struct arguments {
    enum { CHARACTER_MODE, WORD_MODE, LINE_MODE } mode;
    bool isCaseInsensitive;
};

static error_t parse_opt(int key, char *arg, struct argp_state *state) {
    struct arguments * arguments = state->input;
    switch (key) {
    case 'c' arguments->mode = COUNT; break;
    case ARGP_KEY_ARG: return 0;
    default: return ARGP_ERR_UNKNOWN;
    }
    return 0;
}

static struct argp argp = { options, parse_opt, args_doc, doc, 0, 0, 0};

int main(int argc, char *argv[])
{

    struct arguments arguments;
    arguments.mode = CHARACTER_MODE;
    argp_parse(&argp, argc, argv, 0, 0, &arguments);
    int i;
    for (i = 1; i < 100; ++i) 
    {
        printf("%d \n", i);
    }
    return 0;

}
