import camelcase

c = camelcase.CamelCase()
txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu consectetur lectus, eget efficitur diam. Nam ac venenatis mi, eget lacinia nisi. Vivamus eu velit sed dolor vestibulum blandit et at dolor. Pellentesque vel mauris gravida, interdum diam tempus, laoreet odio. Nunc facilisis semper facilisis. Vivamus in pellentesque nisi. Donec vel pellentesque neque. Praesent volutpat tempor turpis at hendrerit. Curabitur id interdum ante. Vivamus gravida eros leo, sed fermentum nulla ultrices eget. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam tristique vitae orci vel pharetra. Sed porttitor, ante in euismod dapibus, lectus nisl ultricies diam, at tincidunt est purus et enim. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Praesent volutpat, diam ac venenatis hendrerit, nibh odio vestibulum mauris, id blandit augue magna eu dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae"
print(c.hump(txt))