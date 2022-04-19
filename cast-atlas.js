import * as std from 'std';

function main() {
    const argv = scriptArgs;
    argv.shift()

    if (argv.length === 0) {
        console.error('Usage: cast-atlas file.atlas');
        return 1;
    }

    const file = std.open(argv[0], 'r');
    console.log(JSON.stringify({ atlas: file.readAsString() }));
}

main();
